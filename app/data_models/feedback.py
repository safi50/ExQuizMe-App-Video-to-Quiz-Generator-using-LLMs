from ..database import db

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transcriptionAccuracy = db.Column(db.Integer, nullable=False)
    quizRelevance = db.Column(db.Integer, nullable=False)
    quizDifficulty = db.Column(db.Integer, nullable=False)
    overallSatisfaction = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    transcription = db.Column(db.Text, nullable = False)
    quiz = db.Column(db.Text, nullable = False)
    complexity = db.Column(db.Text, nullable = False)
    quizType = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f'<Feedback {self.id}>'