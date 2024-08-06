import os
from .conversation import Conversation
from .openai_interface import OpenAIInterface
from data_processing.url_scraper import scrape_url
from data_processing.pdf_extractor import extract_pdf_text
from database.db_manager import DatabaseManager

class Chatbot:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key no proporcionada")
        self.conversation = Conversation()
        self.openai = OpenAIInterface(api_key)
        self.db = DatabaseManager()
        self.current_pdf = None

    def process_input(self, user_input, context=None):
        try:
            if context == 'url':
                if user_input.lower().endswith('.pdf'):
                    return "Esta URL parece ser un PDF. Por favor, usa la opción 'Subir PDF' para procesarlo."
                content = scrape_url(user_input)
                self.db.save_content(user_input, content)
                return f"He guardado la información de la URL: {user_input}. Puedes hacerme preguntas sobre su contenido."
            elif context == 'pdf':
                self.current_pdf = user_input
                content = self.db.get_content(self.current_pdf)
                if content:
                    self.conversation.add_message("system", f"Contexto del PDF '{self.current_pdf}': {content[:1000]}...")
                    return f"He cargado el contenido del PDF '{self.current_pdf}'. ¿Qué te gustaría saber sobre él?"
                else:
                    return f"No se encontró información sobre el PDF '{self.current_pdf}'. Por favor, asegúrate de haberlo subido correctamente."

            # Si no es un nuevo contexto, asumimos que es una pregunta sobre el PDF actual
            if self.current_pdf:
                content = self.db.get_content(self.current_pdf)
                if content:
                    self.conversation.add_message("system", f"Contexto del PDF '{self.current_pdf}': {content[:1000]}...")
                    self.conversation.add_message("user", user_input)
                    response = self.openai.generate_response(self.conversation.get_context())
                    self.conversation.add_message("assistant", response)
                    return response
                else:
                    return f"No se encontró información sobre el PDF actual. Por favor, sube un PDF primero."
            else:
                return "No hay un PDF cargado actualmente. Por favor, sube un PDF primero."

        except Exception as e:
            return f"Error al procesar la entrada: {str(e)}"

    def process_pdf(self, file_path):
        try:
            content = extract_pdf_text(file_path)
            filename = os.path.basename(file_path)
            self.db.save_content(filename, content)
            self.current_pdf = filename
            return f"PDF '{filename}' procesado y guardado con éxito. Puedes hacerme preguntas sobre su contenido."
        except Exception as e:
            return f"Error al procesar el PDF: {str(e)}"