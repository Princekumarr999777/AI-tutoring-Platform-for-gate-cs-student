from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from src.core.config import settings
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str: return pwd.hash(password)
def verify_password(password: str, hashed_password: str) -> bool: return pwd.verify(password, hashed_password)
def _token(subject: str, kind: str, expires: timedelta) -> str:
    now = datetime.now(timezone.utc)
    return jwt.encode({"sub": subject, "type": kind, "iat": now, "exp": now + expires}, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
def create_access_token(subject: str) -> str: return _token(subject, "access", timedelta(minutes=settings.access_token_minutes))
def create_refresh_token(subject: str) -> str: return _token(subject, "refresh", timedelta(days=settings.refresh_token_days))
def decode_token(token: str):
    try: return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    except JWTError as exc: raise ValueError("Invalid or expired token") from exc
