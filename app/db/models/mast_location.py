from sqlalchemy import Table 

from app.db.database import Base, metadata 

class Mast_Location(Base):
    """Map an existing database table(Mast_Location)"""
    __table__ = Table("Mast_Location", metadata, autoload=True)

    # Returning table column names:
    # print(Mast_Location.__table__.columns.keys())