class Conversation:
    def __init__(self):
        # Initializes the class with an empty list to store messages
        self.messages = []

    def add_message(self, role, content):
        # Adds a message to the list of messages
        self.messages.append({"role": role, "content": content})

    def get_context(self):
        # Returns the list of stored messages
        return self.messages