from app import create_app, db
from app.models import Question

def add_questions():
    app = create_app()
    with app.app_context():
        Question.query.delete()
        
        discord_questions = [
            {
                "category": "discord",
                "question_text": "Discord.py'da bir bot nasıl oluşturulur?",
                "options": [
                    "Bot() sınıfını kullanarak",
                    "Client() sınıfını kullanarak",
                    "commands.Bot() sınıfını kullanarak",
                    "discord.Client() sınıfını kullanarak"
                ],
                "correct_answer": 2,
                "explanation": "Discord.py'da bot oluşturmak için commands.Bot() sınıfı kullanılır."
            },
            {
                "category": "discord",
                "question_text": "Bir Discord botunun komutları hangi dekoratör ile tanımlanır?",
                "options": [
                    "@bot.command()",
                    "@discord.command",
                    "@client.command",
                    "@commands.command"
                ],
                "correct_answer": 0,
                "explanation": "Discord.py'da komutlar @bot.command() dekoratörü ile tanımlanır."
            },
            {
                "category": "discord",
                "question_text": "Discord.py'da bir mesaja nasıl tepki (reaction) eklenir?",
                "options": [
                    "message.react(emoji)",
                    "message.add_reaction(emoji)",
                    "message.reaction.add(emoji)",
                    "message.emoji.add(emoji)"
                ],
                "correct_answer": 1,
                "explanation": "Mesajlara tepki eklemek için message.add_reaction(emoji) metodu kullanılır."
            },
            {
                "category": "discord",
                "question_text": "Discord.py'da bir kanaldan mesaj silmek için hangi metod kullanılır?",
                "options": [
                    "channel.remove_messages()",
                    "channel.delete_messages()",
                    "channel.purge()",
                    "channel.clear()"
                ],
                "correct_answer": 2,
                "explanation": "Kanaldan mesaj silmek için channel.purge() metodu kullanılır."
            },
            {
                "category": "discord",
                "question_text": "Discord.py'da bir üyeye rol vermek için hangi metod kullanılır?",
                "options": [
                    "member.give_role(role)",
                    "member.add_role(role)",
                    "member.add_roles(role)",
                    "member.roles.add(role)"
                ],
                "correct_answer": 3,
                "explanation": "Üyeye rol vermek için member.roles.add(role) metodu kullanılır."
            }
        ]

        flask_questions = [
            {
                "category": "flask",
                "question_text": "Flask'ta yeni bir route nasıl tanımlanır?",
                "options": [
                    "@app.route('/path')",
                    "@flask.route('/path')",
                    "@route('/path')",
                    "app.add_route('/path')"
                ],
                "correct_answer": 0,
                "explanation": "Flask'ta yeni route'lar @app.route() dekoratörü ile tanımlanır."
            },
            {
                "category": "flask",
                "question_text": "Flask'ta form verilerine nasıl erişilir?",
                "options": [
                    "form.get_data()",
                    "request.form.get()",
                    "flask.form.data",
                    "request.get_form()"
                ],
                "correct_answer": 1,
                "explanation": "Form verilerine request.form.get() ile erişilir."
            },
            {
                "category": "flask",
                "question_text": "Flask'ta şablon dosyaları hangi fonksiyon ile render edilir?",
                "options": [
                    "flask.render()",
                    "template.render()",
                    "render_template()",
                    "flask.template()"
                ],
                "correct_answer": 2,
                "explanation": "Şablon dosyaları render_template() fonksiyonu ile render edilir."
            },
            {
                "category": "flask",
                "question_text": "Flask'ta oturum verilerine nasıl erişilir?",
                "options": [
                    "flask.session",
                    "app.session",
                    "request.session",
                    "session"
                ],
                "correct_answer": 3,
                "explanation": "Oturum verilerine session nesnesi ile erişilir."
            },
            {
                "category": "flask",
                "question_text": "Flask'ta bir Blueprint nasıl kaydedilir?",
                "options": [
                    "flask.register_blueprint()",
                    "app.add_blueprint()",
                    "app.register_blueprint()",
                    "blueprint.register()"
                ],
                "correct_answer": 2,
                "explanation": "Blueprint'ler app.register_blueprint() ile kaydedilir."
            }
        ]

        ai_questions = [
            {
                "category": "ai",
                "question_text": "Yapay sinir ağlarında aktivasyon fonksiyonu ne işe yarar?",
                "options": [
                    "Veriyi normalize eder",
                    "Nöronun çıktısını belirler",
                    "Ağırlıkları günceller",
                    "Hata oranını hesaplar"
                ],
                "correct_answer": 1,
                "explanation": "Aktivasyon fonksiyonu, nöronun girdilerini işleyerek çıktısını belirler."
            },
            {
                "category": "ai",
                "question_text": "Hangi öğrenme türünde etiketli veri kullanılır?",
                "options": [
                    "Denetimsiz öğrenme",
                    "Pekiştirmeli öğrenme",
                    "Denetimli öğrenme",
                    "Yarı denetimli öğrenme"
                ],
                "correct_answer": 2,
                "explanation": "Denetimli öğrenmede etiketli veri kullanılır."
            },
            {
                "category": "ai",
                "question_text": "Gradyan inişi (gradient descent) ne işe yarar?",
                "options": [
                    "Veri ön işleme",
                    "Model optimizasyonu",
                    "Veri augmentasyonu",
                    "Model değerlendirme"
                ],
                "correct_answer": 1,
                "explanation": "Gradyan inişi, model parametrelerini optimize etmek için kullanılır."
            },
            {
                "category": "ai",
                "question_text": "Overfitting (aşırı öğrenme) nedir?",
                "options": [
                    "Modelin eğitim verisini ezberlemesi",
                    "Modelin yeterince öğrenememesi",
                    "Modelin çok yavaş öğrenmesi",
                    "Modelin hiç öğrenememesi"
                ],
                "correct_answer": 0,
                "explanation": "Overfitting, modelin eğitim verisini ezberlediği durumdur."
            },
            {
                "category": "ai",
                "question_text": "Hangi katman türü görüntü işlemede sıklıkla kullanılır?",
                "options": [
                    "Dense",
                    "Recurrent",
                    "Convolutional",
                    "Embedding"
                ],
                "correct_answer": 2,
                "explanation": "Convolutional (evrişimli) katmanlar görüntü işlemede yaygın kullanılır."
            }
        ]

        cv_questions = [
            {
                "category": "cv",
                "question_text": "OpenCV'de bir görüntü nasıl okunur?",
                "options": [
                    "cv2.readImage()",
                    "cv2.imread()",
                    "cv2.load()",
                    "cv2.open()"
                ],
                "correct_answer": 1,
                "explanation": "OpenCV'de görüntüler cv2.imread() fonksiyonu ile okunur."
            },
            {
                "category": "cv",
                "question_text": "Hangi renk uzayı OpenCV'de varsayılan olarak kullanılır?",
                "options": [
                    "RGB",
                    "BGR",
                    "HSV",
                    "GRAY"
                ],
                "correct_answer": 1,
                "explanation": "OpenCV varsayılan olarak BGR renk uzayını kullanır."
            },
            {
                "category": "cv",
                "question_text": "Görüntü üzerinde gürültüyü azaltmak için hangi işlem kullanılır?",
                "options": [
                    "Keskinleştirme",
                    "Eşikleme",
                    "Bulanıklaştırma",
                    "Kenar tespiti"
                ],
                "correct_answer": 2,
                "explanation": "Gürültüyü azaltmak için bulanıklaştırma (blur) işlemi kullanılır."
            },
            {
                "category": "cv",
                "question_text": "Canny kenar dedektörü ne için kullanılır?",
                "options": [
                    "Yüz tespiti",
                    "Kenar tespiti",
                    "Nesne tanıma",
                    "Renk segmentasyonu"
                ],
                "correct_answer": 1,
                "explanation": "Canny algoritması görüntüdeki kenarları tespit etmek için kullanılır."
            },
            {
                "category": "cv",
                "question_text": "Görüntü piramitleri ne için kullanılır?",
                "options": [
                    "Görüntü sıkıştırma",
                    "Çoklu ölçek analizi",
                    "Renk düzeltme",
                    "Histogram eşitleme"
                ],
                "correct_answer": 1,
                "explanation": "Görüntü piramitleri çoklu ölçek analizi için kullanılır."
            }
        ]

        nlp_questions = [
            {
                "category": "nlp",
                "question_text": "Tokenizasyon nedir?",
                "options": [
                    "Metni küçük harfe çevirme",
                    "Metni kelimelere ayırma",
                    "Metni temizleme",
                    "Metni sınıflandırma"
                ],
                "correct_answer": 1,
                "explanation": "Tokenizasyon, metni anlamlı parçalara (token) ayırma işlemidir."
            },
            {
                "category": "nlp",
                "question_text": "Stop words (durma kelimeleri) nedir?",
                "options": [
                    "Özel isimler",
                    "Teknik terimler",
                    "Sık kullanılan anlamsız kelimeler",
                    "Noktalama işaretleri"
                ],
                "correct_answer": 2,
                "explanation": "Stop words, metinde sık geçen ancak anlam taşımayan kelimelerdir."
            },
            {
                "category": "nlp",
                "question_text": "Lemmatization ne işe yarar?",
                "options": [
                    "Kelimeleri köklerine ayırır",
                    "Kelimeleri sayar",
                    "Cümleleri ayırır",
                    "Metni temizler"
                ],
                "correct_answer": 0,
                "explanation": "Lemmatization, kelimeleri anlamlı köklerine indirger."
            },
            {
                "category": "nlp",
                "question_text": "TF-IDF ne için kullanılır?",
                "options": [
                    "Metin özetleme",
                    "Duygu analizi",
                    "Kelime önemi hesaplama",
                    "Cümle ayırma"
                ],
                "correct_answer": 2,
                "explanation": "TF-IDF, kelimelerin dokümandaki önemini hesaplamak için kullanılır."
            },
            {
                "category": "nlp",
                "question_text": "Word embedding nedir?",
                "options": [
                    "Kelime sayma",
                    "Kelimeleri vektörlere dönüştürme",
                    "Kelime temizleme",
                    "Kelime sıralama"
                ],
                "correct_answer": 1,
                "explanation": "Word embedding, kelimeleri sayısal vektörlere dönüştürme işlemidir."
            }
        ]

        all_questions = discord_questions + flask_questions + ai_questions + cv_questions + nlp_questions
        for q in all_questions:
            question = Question(
                category=q["category"],
                question_text=q["question_text"],
                options=q["options"],
                correct_answer=q["correct_answer"],
                explanation=q["explanation"]
            )
            db.session.add(question)
        
        db.session.commit()
        print(f"Toplam {len(all_questions)} soru eklendi.")

if __name__ == "__main__":
    add_questions() 