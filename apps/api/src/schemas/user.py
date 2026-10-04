from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr
class ProfileRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    full_name: str
class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    role: str
    created_at: datetime
    profile: ProfileRead | None = None
