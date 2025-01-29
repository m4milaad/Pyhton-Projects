class QuizBrain:
    def __init__(self, bank):
        self.question_number = 0
        self.question_list = bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user = input(f"Q{self.question_number + 1}. {self.question_list[self.question_number].question} (True/False)")
        self.check_answer(user.lower(), self.question_list[self.question_number].answer.lower())
        self.question_number += 1
        


    def check_answer(self, user, answer):
        if user == answer:
            self.score += 1
            print("That's right")
        else:
            print("That's Wrong")
        print(f"The correct answer was {answer.title()}")
        print(f"Your score is {self.score}/{self.question_number}\n\n")