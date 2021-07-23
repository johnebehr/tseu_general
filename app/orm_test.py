from sqlalchemy import MetaData, Table
from sqlalchemy.ext.automap import automap_base

from app.db.database import engine, SessionLocal


# membership_meta = MetaData(engine)

# members = Table("Members", membership_meta, autoload=True)

session = SessionLocal()

# results = session.query(members).filter(members.columns.Last_Name == "Behr")

# print(results.all())

Base = automap_base()
Base.prepare(engine, reflect=True)

Members = Base.classes.Members
Location = Base.classes.Mast_Location

def as_dict(obj) -> dict:
    data = obj.__dict__ 
    data.pop('_sa_instance_state')
    return data

# for c in [Members, Location]:
#     c.as_dict = as_dict

q = session.query(Members.First_Name, Members.Last_Name, Location.Location_Name)
q = q.filter(Members.Last_Name == "Behr", Members.Location_code == Location.Location_Code)

print(q)