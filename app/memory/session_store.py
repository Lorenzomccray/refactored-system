class SessionStore:
    def __init__(self):
        self.memory = []

    def save(self, data):
        self.memory.append(data)

    def get_all(self):
        return self.memory
