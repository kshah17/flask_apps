from app import db

db.drop_all()
db.create_all()

testuser = Users(first_name='Kev')
db.session.add(testuser)
db.session.commit()

