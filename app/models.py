from app import db
from datetime import datetime

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    options = db.Column(db.JSON, nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)
    explanation = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'question_text': self.question_text,
            'options': self.options
        }

    def check_answer(self, selected_answer):
        return selected_answer == self.correct_answer

    @staticmethod
    def get_questions_by_category(category, limit=5):
        return Question.query.filter_by(category=category).order_by(db.func.random()).limit(limit).all()

class UserScore(db.Model):
    __tablename__ = 'user_score'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    max_score = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def get_high_score(session_id):
        return UserScore.query.filter_by(session_id=session_id).order_by(UserScore.percentage.desc()).first()

    @staticmethod
    def get_global_high_score():
        return UserScore.query.order_by(UserScore.percentage.desc()).first() 