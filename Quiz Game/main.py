from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import art
question_bank = []
for question in question_data:
    question_object = Question(question=question["text"], answer=question["answer"])
    question_bank.append(question_object)
print(art)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

if quiz.score == quiz.question_number:
    print("You won")
