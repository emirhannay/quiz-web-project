from flask import Blueprint, render_template, jsonify, request, session
from app.models import Question, UserScore
from app import db
import uuid

main = Blueprint('main', __name__)

CATEGORIES = ['discord.py', 'flask', 'ai', 'cv', 'nlp']
QUESTIONS_PER_CATEGORY = 5

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/quiz')
def quiz():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return render_template('quiz.html')

@main.route('/api/high-score')
def get_high_score():
    global_best = UserScore.get_global_high_score()
    personal_best = None
    if 'user_id' in session:
        personal_best = UserScore.get_high_score(session['user_id'])
    
    return jsonify({
        'global_best': global_best.percentage if global_best else 0,
        'personal_best': personal_best.percentage if personal_best else 0
    })

@main.route('/api/questions')
def get_questions():
    all_questions = []
    for category in CATEGORIES:
        questions = Question.get_questions_by_category(category, QUESTIONS_PER_CATEGORY)
        all_questions.extend([q.to_dict() for q in questions])
    return jsonify(all_questions)

@main.route('/api/check-answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    question = Question.query.get(data['question_id'])
    if not question:
        return jsonify({'error': 'Soru bulunamadı'}), 404
    
    is_correct = question.check_answer(data['selected_answer'])
    return jsonify({'correct': is_correct})

@main.route('/api/save-score', methods=['POST'])
def save_score():
    try:
        data = request.get_json()
        score = data['score']
        max_score = data['max_score']
        percentage = (score / max_score) * 100

        user_score = UserScore(
            session_id=session['user_id'],
            score=score,
            max_score=max_score,
            percentage=percentage
        )
        db.session.add(user_score)
        db.session.commit()

        personal_best = UserScore.get_high_score(session['user_id'])
        global_best = UserScore.get_global_high_score()

        return jsonify({
            'personal_best': personal_best.percentage if personal_best else 0,
            'global_best': global_best.percentage if global_best else 0
        })
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Skor kaydedilirken bir hata oluştu'}), 500 