from openai import OpenAI

class OpenAIInterface:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, messages):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content