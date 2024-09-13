from core import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type=db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password=db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(50), nullable=True)
    dob = db.Column(db.String(50), nullable=True)
    mobile = db.Column(db.Integer, nullable=True)
    user_id=db.Column(db.String(10), nullabe=True)
    token=db.Column(db.String(20), nullable=True)