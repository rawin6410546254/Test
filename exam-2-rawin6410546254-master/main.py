import csv
from question_model import Question
from quiz_control import QuizControl
questions = []


difficulty = input("Select difficulty (easy, medium, hard): ")
if difficulty == "easy":
    for i in range(8):
        f"Question: {questions == 'easy'}\nChoice 1: {questions == 'correct_answer'}"

elif difficulty == "medium":
    for i in range(9):
        f"Question: {questions == 'medium'}"

elif difficulty == "hard":
    for i in range(3):
        f"Question: {questions == 'hard'}"







quiz = QuizControl(questions)
while quiz.has_question():
    quiz.next()
