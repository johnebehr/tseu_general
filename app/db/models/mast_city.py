from sqlalchemy import Table

from app.db.database import Base, metadata

class Mast_City(Base):
    """Map an existing database table (Mast_City)"""
    __table__ = Table("Mast_City", metadata, autoload=True)

    # Returning table column names:
    # print(Mast_City.__table__.columns.keys())