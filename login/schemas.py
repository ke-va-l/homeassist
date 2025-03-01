from pydantic import BaseModel, EmailStr
from typing import Optional

class CompanyCreate(BaseModel):
    company_name: str
    owner_name: str
    opening_time: str
    closing_time: str
    website: Optional[str] = None
    address: str
    service_area: str
    city: str
    email: EmailStr
    mobile_number: str
    whatsapp_number: Optional[str] = None
    experience: int
    description: Optional[str] = None
    license_certificate: Optional[str] = None
    last_10_customers: Optional[str] = None
    password: str

class CustomerCreate(BaseModel):
    full_name: str
    city: str
    number: str
    email: EmailStr  # ✅ Added email field
    address: str
    description: Optional[str] = None
    password: str

class CustomerLogin(BaseModel):
    email: EmailStr  # ✅ Updated to use email for login
    password: str


class CompanyLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
