

from sqlalchemy import select, inspect

from sqlalchemy.orm import session
from app.db.database import SessionLocal, metadata
from app.db.models.members import Members 
from app.db.models.mast_location import Mast_Location

def show_query_results(results):
    for row in results:
        print(row.First_Name)

session = SessionLocal()
stmt = select(Members.First_Name, Members.Last_Name).\
    where(Members.Last_Name == "Jones")

results = session.execute(stmt)

# cols_to_map = ("first_name", "last_name")
# cols_to_map = tuple(session.execute(stmt)._metadata.keys)
# cols_to_map = tuple(results._metadata.keys)

# Function that will convert a row tuple to a dict
# def as_dict(tup) -> dict:
#     if len(cols_to_map) == len(tup):
#         return {cols_to_map[i]:tup[i] for i, _ in enumerate(tup)}
#     else:
#         raise ValueError("Tuples not same length.")

# Take the results and print a dict for each row
# for row in results:
#     print(as_dict(row))

print("="*80)

# print(stmt.keys())
# print(Members.__table__.columns.keys())
# print(tuple(session.execute(stmt)._metadata.keys))
# print(tuple(results._metadata.keys))

# for result in results:
#     print(result._asdict())

# b = results.all()
# print(b[0])

for result in results.all():
    print(dict(zip(result.keys(), result)))

print("="*80)