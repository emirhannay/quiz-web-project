from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)  # discord.py, flask, ai, cv, nlp
    question_text = db.Column(db.Text, nullable=False)
    options = db.Column(db.JSON, nullable=False)  # ["seçenek1", "seçenek2", "seçenek3", "seçenek4"]
    correct_answer = db.Column(db.Integer, nullable=False)  # 0-3 arası index
    explanation = db.Column(db.Text)  # Opsiyonel açıklama
    
    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'question_text': self.question_text,
            'options': self.options,
            'explanation': self.explanation
        }
    
    @staticmethod
    def get_questions_by_category(category, limit=5):
        """Belirli bir kategoriden rastgele soru seçer"""
        return Question.query.filter_by(category=category)\
            .order_by(db.func.random())\
            .limit(limit)\
            .all()
    
    def check_answer(self, user_answer):
        """Kullanıcı cevabının doğruluğunu kontrol eder"""
        return user_answer == self.correct_answer 