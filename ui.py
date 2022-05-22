from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


# TODO -4 TO get the question text from quiz_brain.next_question(), we have to create a function in ui
#  and config canvas text called get_next_question()

# TODO -5 creating a instance quiz and assigning it to parameter called quizbrain
#  quizbrain = parameter
#  quiz = class instance
#  passing quiz_brain object as parameter to quizInterface class object
#  quizbrain datatype is QuizBrain ie quizbrain is a parameter with datatype of class quizBrain
#  cannot pass other datatype

# TODO - 6 Creating tkinter window, and other GUI widgets
class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="questions",
                                                     fill=THEME_COLOR,
                                                     font=("arial", 20, "italic"))
        self.canvas.grid(pady=50, row=1, column=0, columnspan=2)

        self.score_label = Label(text=f"score: 0", bg=THEME_COLOR, anchor="center", fg="white")
        self.score_label.grid(row=0, column=1)

        right_image = PhotoImage(file=r"images/true.png")
        self.r_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.r_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file=r"images/false.png")
        self.w_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.w_button.grid(row=2, column=1)
        # TODO - 8 calling the get_next_question() before mainloop inside init method
        self.get_next_question()

        self.window.mainloop()

    # TODO - 7 to create this method to config canvas text with the q_text returned by quiz_brain.next_question method
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.r_button.config(state='active')
            self.w_button.config(state="active")
        else:
            self.canvas.itemconfig(self.question_text, text="Successfully completed the quiz Hurray!!")

    # TODO - 8 to realise that the r_button or w_button clicked and check the answer
    #  create two function True pressed or fasle_pressed
    #  create a variable is_correct assging to a method called check answer
    #  after calling check_answer with user_answer as string of True or False, call give_feedback(is_coorect)
    def true_pressed(self):
        is_correct = self.quiz.check_answer(user_answer="true")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer(user_answer="false")
        self.give_feedback(is_correct)
    # TODO -10 changing the background according to right answer
    #  to eliminate the fast clicking by user, disabled button during this method
    #  is_correct passed from true_pressed or false_pressed depends on the button we press
    #  if is_correct is True [ie user_answer == correct answer from question_data] --> green
    #  if is_correct is False [ie user_answer != correct answer from question_data] --> red
    #  after method for looping the question by calling get_next_question

    def give_feedback(self, is_correct):
        self.r_button.config(state='disabled')
        self.w_button.config(state="disabled")
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
