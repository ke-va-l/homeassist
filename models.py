from sqlalchemy import Column, Integer, String, Text
from database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True, nullable=False)
    owner_name = Column(String, nullable=False)
    opening_time = Column(String, nullable=False)
    closing_time = Column(String, nullable=False)
    website = Column(String, nullable=True)
    address = Column(Text, nullable=False)
    service_area = Column(Text, nullable=False)
    city = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    mobile_number = Column(String, unique=True, nullable=False)
    whatsapp_number = Column(String, nullable=True)
    experience = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    license_certificate = Column(String, nullable=True)
    last_10_customers = Column(Text, nullable=True)
    hashed_password = Column(String, nullable=False)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    number = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    hashed_password = Column(String, nullable=False)

