import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config:
    SECRET_KEY = 'emirhan-quiz-app-secret-key-123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'quiz.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 