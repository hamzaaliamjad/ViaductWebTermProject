from .db import db


class Student(db.Document):
    s_id = db.IntField(Unique=True, default=1000, auto_incremet=True)
    s_name = db.StringField(required=True)
    s_rollno = db.StringField(required=True)
    s_email = db.StringField(required=True)
    s_password = db.StringField(required=True)
    s_address = db.StringField(required=True)
    s_phoneNo = db.StringField(required=True)
    s_gender = db.StringField(required=True)
    s_semester = db.IntField(required=True)
    s_cgpa = db.IntField(required=True)
    s_degree = db.StringField(required=True)
    s_skills = db.StringField()
    s_intro = db.StringField()
    s_interest = db.StringField()
    s_pic = db.StringField()
    s_resume = db.StringField()
