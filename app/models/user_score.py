from datetime import datetime
from app import db

class UserScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    max_score = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @staticmethod
    def get_high_score(session_id):
        return UserScore.query\
            .filter_by(session_id=session_id)\
            .order_by(UserScore.percentage.desc())\
            .first()

    @staticmethod
    def get_global_high_score():
        return UserScore.query\
            .order_by(UserScore.percentage.desc())\
            .first()

    def to_dict(self):
        return {
            'score': self.score,
            'max_score': self.max_score,
            'percentage': self.percentage,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } 