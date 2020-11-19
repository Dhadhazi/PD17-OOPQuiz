class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, answer):
        return answer == self.answer

    def get_question(self):
        return self.text