from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Company, Customer
from login.schemas import CompanyCreate, CustomerCreate, CompanyLogin, CustomerLogin, Token
from login.auth import hash_password, verify_password, create_access_token
from datetime import timedelta

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register/company")
def register_company(company: CompanyCreate, db: Session = Depends(get_db)):
    if db.query(Company).filter(Company.email == company.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_company = Company(
        company_name=company.company_name,
        owner_name=company.owner_name,
        opening_time=company.opening_time,
        closing_time=company.closing_time,
        website=company.website,
        address=company.address,
        service_area=company.service_area,
        city=company.city,
        email=company.email,
        mobile_number=company.mobile_number,
        whatsapp_number=company.whatsapp_number,
        experience=company.experience,
        description=company.description,
        license_certificate=company.license_certificate,
        last_10_customers=company.last_10_customers,
        hashed_password=hash_password(company.password)
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return {"message": "Company registered successfully"}


@app.post("/register/customer")
def register_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    if db.query(Customer).filter(Customer.email == customer.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    if db.query(Customer).filter(Customer.number == customer.number).first():
        raise HTTPException(status_code=400, detail="Number already registered")
    
    new_customer = Customer(
        full_name=customer.full_name,
        city=customer.city,
        number=customer.number,
        email=customer.email,
        address=customer.address,
        description=customer.description,
        hashed_password=hash_password(customer.password)
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return {"message": "Customer registered successfully"}


@app.post("/login/customer")
def login_customer(credentials: CustomerLogin, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.email == credentials.email).first() 
    if not customer or not verify_password(credentials.password, customer.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": credentials.email}, timedelta(minutes=60))
    return Token(access_token=access_token, token_type="bearer")



@app.post("/login/company")
def login_company(credentials: CompanyLogin, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.email == credentials.email).first()
    if not company or not verify_password(credentials.password, company.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": credentials.email}, timedelta(minutes=60))
    return Token(access_token=access_token, token_type="bearer")

