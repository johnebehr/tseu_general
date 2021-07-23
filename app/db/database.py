import yaml
from yaml.loader import FullLoader

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def get_settings() -> dict:
    # Open the settings file in the root directory 
    with open("settings.yaml") as f:
        conns = yaml.load(f, FullLoader)

        # Get the Membership connection definitions 
        return conns["membership_pymysql"]

# Create a database URL for SQLAlchemy
SQL_ALCHEMY_DATABASE_URL = URL(**get_settings())

# Create the SQLAlchemy engine 
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

# Instantiate the base parent class
Base = declarative_base()
metadata = MetaData(bind=engine)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)