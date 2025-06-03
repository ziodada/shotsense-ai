import random

def analyze_shooting_form(filename, shooting_arm):
    """Analisi rapida del tiro"""
    
    # Simula analisi angolo ginocchio
    knee_angle = round(random.uniform(75, 105), 1)
    
    # Calcola score
    optimal_angle = 90
    angle_deviation = abs(knee_angle - optimal_angle)
    
    if angle_deviation <= 5:
        score = random.randint(85, 95)
    elif angle_deviation <= 10:
        score = random.randint(70, 85)
    else:
        score = random.randint(50, 70)
    
    # Valutazione
    if 85 <= knee_angle <= 95:
        evaluation = "Ottimo"
        color = "#27ae60"
    elif 80 <= knee_angle <= 100:
        evaluation = "Buono" 
        color = "#f39c12"
    else:
        evaluation = "Da migliorare"
        color = "#e74c3c"
    
    return {
        'score': score,
        'knee_bend_angle': knee_angle,
        'evaluation': evaluation,
        'color': color,
        'shooting_arm': shooting_arm,
        'filename': filename
    }

def generate_shooting_feedback(data):
    """Genera feedback veloce"""
    score = data.get('score', 75)
    arm = data.get('shooting_arm', 'RIGHT')
    knee_angle = data.get('knee_bend_angle', 90)
    
    if score >= 85:
        return f"🔥 Ottima tecnica con il braccio {arm}! L'angolo ginocchio di {knee_angle}° è eccellente. Continua così per mantenere la consistenza. Focus sulla concentrazione mentale."
    elif score >= 70:
        return f"💪 Buona tecnica con il braccio {arm}. L'angolo ginocchio di {knee_angle}° è buono. Lavora sulla ripetibilità e coordinazione per migliorare ulteriormente."
    else:
        return f"🏀 Tecnica da perfezionare con il braccio {arm}. L'angolo ginocchio di {knee_angle}° necessita correzioni. Concentrati sui fondamentali: postura e allineamento."
