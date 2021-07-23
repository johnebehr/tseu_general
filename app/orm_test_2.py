from sqlalchemy import MetaData, Table
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm.session import sessionmaker 

from app.db.database import engine, SessionLocal 

membership_meta = MetaData(engine)

members = Table("Members", membership_meta, autoload=True)
mast_location = Table("Mast_Location", membership_meta, autoload=True)

session = SessionLocal()

# results = session.query(members).filter(members.columns.Last_Name == "Jones")

# print(results.all())
# for row in results:
#     print(dict(row))

records = session.query(members, mast_location).\
    filter(members.columns.Location_code == mast_location.columns.Location_Code).\
    filter(mast_location.columns.Agency_Code == 4401).all()

# for instance in session.query(members).filter(members.columns.Last_Name == "Jones"):
#     print(instance.First_Name, instance.Last_Name)

for record in records:
    recordObject = {
        "first_name": record.First_Name, 
        "last_name": record.Last_Name
    }
    print(recordObject)