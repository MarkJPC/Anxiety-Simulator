from app import db, login_manager, app
from datetime import datetime
from flask_login import UserMixin
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# create classes which make up the tables of the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # this is how our object is printed
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    questions = db.relationship('Question', backref='exam', lazy=True)

    def __repr__(self):
        return f"Exam('{self.title}', '{self.date_posted}')"

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    time_allocated = db.Column(db.Integer, nullable=False)
    time_spent = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Question('{self.text}', '{self.topic}', '{self.time_allocated}', '{self.time_spent}')"


# this will represent an instance of a user taking an exam
class UserExam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)
    questions = db.relationship('UserQuestion', backref='user_exam', lazy=True)
    score = db.Column(db.Integer, nullable=False)
    time_started = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_completed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_spent = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"UserExam('{self.user_id}', '{self.exam_id}', '{self.score}', '{self.time_started}', '{self.time_completed}', '{self.time_spent}')"


# this will represent an instance of a user answering a question
class UserQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_exam_id = db.Column(db.Integer, db.ForeignKey('user_exam.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    time_started = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_completed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_spent = db.Column(db.Integer, nullable=False)
    is_saved = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"UserQuestion('{self.user_exam_id}', '{self.question_id}', '{self.time_started}', '{self.time_completed}', '{self.time_spent}', '{self.is_saved}')"
