from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class StudentModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    program = db.Column(db.String(80))

    def __init__(self, student_id, name, age, program):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.program = program

    def __repr__(self):
        return f"{self.name}:{self.student_id}"
