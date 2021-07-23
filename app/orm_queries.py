from sqlalchemy import select


from app.db.database import SessionLocal
from app.db.models.members import Members
from app.db.models.mast_location import Mast_Location

session = SessionLocal()

# Select yourself from the Members table 
stmt_01 = select(Members.First_Name, Members.Last_Name).\
    where(Members.Last_Name == "Behr")

results_01 = session.execute(stmt_01)

for result in results_01:
    print(dict(zip(result.keys(), result)))

print("="*80)

# Multi-Table Query 
stmt_02 = select(Members.First_Name, Members.Last_Name, Mast_Location.Location_Name).\
    join(Mast_Location, Members.Location_code == Mast_Location.Location_Code).\
    where(Members.Zero_Dues_Code == "OK", Mast_Location.Agency_Code == 4401)

results_02 = session.execute(stmt_02)

# for result in results_02:
#     print(dict(zip(result.keys(), result)))

# print("="*80)

result_dict_list = [dict(zip(result.keys(), result)) for result in results_02]

print(result_dict_list)
print("="*80)

for result in results_02:
    # print(dict(zip(result.keys(), result)))
    print(result)

print("="*80)
print(results_02)
print(result_dict_list)