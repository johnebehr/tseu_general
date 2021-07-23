from sqlalchemy import Table

from app.db.database import Base, metadata

class Members(Base):
    """Map an existing database table (Members)"""
    __table__ = Table("Members", metadata, autoload=True)

    # Returning table column names:
    # print(Members.__table__.columns.keys())