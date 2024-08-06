import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No se ha configurado OPENAI_API_KEY. Por favor, configúrala en los secretos de Replit.")

DATABASE_PATH = os.getenv('DATABASE_PATH', 'chatbot.db')
SECRET_KEY = os.getenv('SECRET_KEY')  # Asegúrate de cambiar esto en producción