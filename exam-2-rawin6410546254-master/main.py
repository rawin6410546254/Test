import csv
from question_model import Question
from quiz_control import QuizControl
questions = []

# Write your code below #


# Write your code above #

quiz = QuizControl(questions)
while quiz.has_question():
    quiz.next()
