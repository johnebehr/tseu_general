from sqlalchemy import MetaData, Table 
from sqlalchemy.orm import create_session 
from sqlalchemy.ext.declarative import declarative_base 

from app.db.database import engine, SessionLocal 

Base = declarative_base()
metadata = MetaData(bind=engine)

class Organizers(Base):
    """Map an existing database table (Mast_Organizer)"""
    __table__=  Table("Mast_Organizer", metadata, autoload=True)

def show_query_result(results):
    for row in results:
        print(row.Organizer_Name)

session = SessionLocal()

results = session.query(Organizers).all()
show_query_result(results)

print("="*79)

def as_dict(obj) -> dict:
    data = obj.__dict__ 
    data.pop('_sa_instance_state')
    return data

print(as_dict(results))
