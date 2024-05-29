from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from env import get_settings

def setup_db():
    settings = get_settings()
    # configure database
    engine = create_engine(settings["SQLALCHEMY_DATABASE_URL"])
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    return { "engine": engine, "SessionLocal": SessionLocal, "Base": Base }
