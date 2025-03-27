from app import create_app, db

def init_db():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Veritabanı başarıyla oluşturuldu!")

if __name__ == "__main__":
    init_db() 