from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from ai_coach import analyze_shooting_form, generate_shooting_feedback

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configura Flask secret key
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

@app.route('/')
def index():
    # Serve index.html direttamente dalla root
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files.get('file')
        arm = request.form.get('shooting_arm', 'RIGHT')
        
        if file:
            print(f"📁 File ricevuto: {file.filename}")
            
            # Analisi AI (il tuo codice che funziona)
            analysis = analyze_shooting_form(file.filename, arm)
            feedback = generate_shooting_feedback(analysis)
            
            # Return JSON per il nuovo frontend
            return jsonify({
                "success": True,
                "score": analysis['score'],
                "level": analysis['level'],
                "level_description": analysis['level_description'],
                "color": analysis['color'],
                "leg_score": analysis['leg_score'],
                "leg_bend_angle": analysis['leg_bend_angle'],
                "elbow_score": analysis['elbow_score'],
                "elbow_alignment": analysis['elbow_alignment'],
                "follow_score": analysis['follow_score'],
                "follow_through": analysis['follow_through'],
                "feedback": feedback
            })
            
        return jsonify({
            "success": False,
            "error": "Nessun file caricato"
        })
    
    except Exception as e:
        print(f"❌ ERRORE: {e}")
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
