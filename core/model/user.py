from core import db
from datetime import datetime
from core.libs.assertions import assert_valid,assert_found
from werkzeug.security import check_password_hash
from core.apis.common import gen_token

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type=db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password=db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(50), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    mobile = db.Column(db.Integer, nullable=True)
    user_id=db.Column(db.String(10), nullable=True)
    token=db.Column(db.String(20), nullable=True)
    date = db.Column(db.TIMESTAMP(timezone=True), default= datetime.utcnow, nullable=False)

    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)
    
    @classmethod
    def UserCheck(cls, data):
        user=cls.filter(cls.email==data['email']).first()
        assert_valid(user is None,"user already exist !!!")
        if 'mobile' in data:
            user=cls.filter(cls.mobile==data['mobile']).first()
            assert_valid(user is None,"user already exist !!!")

    @classmethod
    def signup(cls,data):
        cls.UserCheck(data)
        if data['type']==1:
            user = cls(type=data['type'],email=data['email'],password=data['password'])
        elif data['type']==2:
            user = cls(type=data['type'],email=data['email'],password=data['password'])
        elif data['type']==4:
            user = cls(type=data['type'],email=data['email'],password=data['password'],user_id=data['user_id'], dob=data['dob'], name=data['name'], mobile=data['mobile'])
        
        db.session.add(user)
        db.session.flush()

    @classmethod
    def login(cls,data):
        user = cls.filter(cls.email==data['email'],cls.type==data['type']).first()
        assert_found(user,"user does not exist !!!")
        assert_valid(check_password_hash(user.password, data['password']),"incorrect password")

    @classmethod
    def forget(cls,data):
        user = cls.filter(cls.email==data['email'],cls.type==data['type']).first()
        assert_found(user,"user does not exist !!!")
        assert_valid(not check_password_hash(user.password, data['password']), "same as password !!!")

    @classmethod
    def change_password(cls,data):
        user=cls.filter(cls.email==data['email'],cls.type==data['type']).first()
        assert_found(user,"user does not exist !!!")
        user.password=data['password']
        db.session.flush()