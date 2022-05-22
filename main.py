from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
# TODO - 1 Question_bank is alist populated by question from Question_data generated from api
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# TODO -2 creating object for QuizBrain class with q_list parameter as question_bank list
quiz = QuizBrain(question_bank)
# TODO -3 passing quizBrain object as input to QuizInterface object --> quiz_ui
quiz_ui = QuizInterface(quiz)
