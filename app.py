from flask import Flask, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os
from ai_coach import analyze_shooting_form, generate_shooting_feedback

load_dotenv()
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    arm = request.form.get('shooting_arm', 'RIGHT')
    
    if file:
        analysis = analyze_shooting_form(file.filename, arm)
        feedback = generate_shooting_feedback(analysis)
        return f"Score: {analysis['score']}/100 - {feedback}"
    return "No file uploaded"

if __name__ == '__main__':
    app.run(debug=True)
