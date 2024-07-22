from flask import request, jsonify, render_template
from . import app, whisper_wrapper, mixtral_wrapper, db
from .data_models import Feedback
import os

@app.route('/', methods=['GET'])
def home():
    """
    Render the frontend.
    """
    return render_template('index.html')

@app.route('/transcribe_video', methods=['POST'])
def transcribe_video():
    """
    Transcribes given video(s) using whisper wrapper.
    Returns a transcription of the input video(s)
    """
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400

    transcriptions = []  # List to hold transcriptions from all videos
    print("here")
    # Process each video file
    for video_file in request.files.getlist('video'):
        video_path = "./temp_video"  # Temporary path for uploaded video
        video_file.save(video_path)
        audio_path = whisper_wrapper.extract_audio_from_video(video_path)
        text = whisper_wrapper.transcribe(audio_path)
        transcriptions.append(text)
        
        # Clean up temporary files
        os.remove(video_path)
        os.remove(audio_path)
    
    # Concatenate all transcriptions into one string
    combined_transcription = " ".join(transcriptions)
    
    return jsonify({'transcription': combined_transcription}), 200

@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    data = request.json
    if not data or 'transcription' not in data:
        return jsonify({'error': 'No transcription provided'}), 400
    
    transcription = data['transcription']
    complexity = data.get('complexity', 'medium')  # Default to 'medium' if not specified
    q_type = data.get('q_type', 'quiz')  # Default to 'quiz' if not specified

    # Correct possible typos made by whisper model during the transcription
    corrected_transcription = mixtral_wrapper.correct_transcription(transcription) 
    # Generate a quiz
    quiz_json = mixtral_wrapper.generate_quiz(corrected_transcription, complexity, q_type)

    return jsonify({'quiz': quiz_json})

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """
    Writes given feedback into local SQLite database.
    Returns a success message upon successful submission.
    """
    feedback_data = request.json
    try:
        feedback_entry = Feedback(
            transcriptionAccuracy=feedback_data['transcriptionAccuracy'],
            quizRelevance=feedback_data['quizRelevance'],
            quizDifficulty=feedback_data['quizDifficulty'],
            overallSatisfaction=feedback_data['overallSatisfaction'],
            comments=feedback_data.get('comments'),
            complexity=feedback_data.get('complexity', 'medium'),
            transcription=feedback_data.get('transcription'),
            quiz=feedback_data.get('quiz'),
            quizType=feedback_data.get('type', 'quiz')
        )
        db.session.add(feedback_entry)
        db.session.commit()
        
        return jsonify({'message': 'Feedback received'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error saving feedback: {e}")
        return jsonify({'error': 'Failed to save feedback'}), 500
