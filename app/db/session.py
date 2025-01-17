from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()  # Ova linija učitava promenljive iz .env fajla

# Citanje iz .env fajla, mora se napraviti fajl
DATABASE_URL = os.getenv("DATABASE_URL")
# Direktan unos
# DATABASE_URL="mysql+mysqlconnector://vozac:vozilo@localhost/voznipark"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()