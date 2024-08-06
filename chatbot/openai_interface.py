from openai import OpenAI

class OpenAIInterface:
    def __init__(self, api_key):
        """
        Inicializa una instancia de OpenAIInterface.
        
        Parametros:
        api_key (str): Clave API para autenticar la cuenta de OpenAI.
        """
        # Inicializa el cliente de OpenAI con la clave API suministrada
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, messages):
        """
        Genera una respuesta usando el modelo gpt-3.5-turbo para los mensajes proporcionados.
        
        Parametros:
        messages (list): Lista de mensajes en formato dict a enviar al modelo.
        
        Retorna:
        str: Contenido del mensaje de la primera opción en la respuesta.
        """
        # Genera una respuesta usando el modelo gpt-3.5-turbo para los mensajes proporcionados
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        # Retorna el contenido del mensaje de la primera opción
        return response.choices[0].message.content