class ConfidenceScore:
    def __init__(self):
        self.score = 0

    def add(self, value):
        self.score += value

    def get_score(self):
        return self.score

    def reset(self):
        self.score = 0