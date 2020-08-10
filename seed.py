from app import app 
from models import db, connect_db,Tech, Project, Task ,Freezer

db.drop_all()
db.create_all()



