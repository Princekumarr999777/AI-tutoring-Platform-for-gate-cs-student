from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from src.core.database import get_db
from src.core.security import create_access_token, create_refresh_token, decode_token, hash_password, verify_password
from src.models.profile import Profile
from src.models.user import User
from src.schemas.auth import RefreshRequest, TokenResponse, UserCreate, UserLogin
from src.schemas.user import UserRead
router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
Db = Annotated[AsyncSession, Depends(get_db)]
oauth = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
async def current_user(token: Annotated[str, Depends(oauth)], db: Db) -> User:
    try:
        claims = decode_token(token)
        if claims.get("type") != "access": raise ValueError()
        user = await db.scalar(select(User).where(User.id == int(claims["sub"])))
        if user: return user
    except (ValueError, KeyError, TypeError): pass
    raise HTTPException(401, detail="Invalid authentication credentials")
def pair(uid: int) -> TokenResponse:
    sub = str(uid)
    return TokenResponse(access_token=create_access_token(sub), refresh_token=create_refresh_token(sub))
@router.post("/register", response_model=UserRead, status_code=201)
async def register(data: UserCreate, db: Db):
    if await db.scalar(select(User.id).where(User.email == data.email.lower())): raise HTTPException(409, detail="Email already registered")
    user = User(email=data.email.lower(), hashed_password=hash_password(data.password))
    user.profile = Profile(full_name=data.full_name)
    db.add(user)
    try: await db.commit()
    except Exception as exc:
        await db.rollback(); raise HTTPException(409, detail="Email already registered") from exc
    await db.refresh(user, attribute_names=["profile"])
    return user
@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin, db: Db):
    user = await db.scalar(select(User).where(User.email == data.email.lower()))
    if not user or not verify_password(data.password, user.hashed_password): raise HTTPException(401, detail="Incorrect email or password")
    return pair(user.id)
@router.post("/refresh", response_model=TokenResponse)
async def refresh(data: RefreshRequest, db: Db):
    try:
        claims = decode_token(data.refresh_token)
        uid = int(claims["sub"])
        if claims.get("type") != "refresh" or not await db.scalar(select(User.id).where(User.id == uid)): raise ValueError()
        return pair(uid)
    except (ValueError, KeyError, TypeError): raise HTTPException(401, detail="Invalid refresh token")
@router.get("/me", response_model=UserRead)
async def me(user: Annotated[User, Depends(current_user)], db: Db):
    return await db.scalar(select(User).options(selectinload(User.profile)).where(User.id == user.id))
