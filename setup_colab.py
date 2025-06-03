# ShotSense AI Setup for Colab
import subprocess
import sys

print("Installing packages...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", 
                      "flask", "flask-cors", "python-dotenv", "groq", "pyngrok"])
print("✅ Setup complete!")
