class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, question_answer):
        if (user_answer.lower() == question_answer.lower()):
            self.score += 1
            print("You got it right!")
        else:
            print("Wrong answer mateee")
        print(f"Your current score is: {self.score}/{self.question_number}\n")