import os 
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI(title = "3-Tier App API")

# Dynamically load the database URL injected by Docker Compose 
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/appdb")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@app.get("/")
def read_root():
    return {"status": "Application Tier is Live"}

@app.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected"}