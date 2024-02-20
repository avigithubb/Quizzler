from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # Defining the type of quiz_brain as QuizBrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizInterface")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.new_word = self.canvas.create_text(150, 120, width=280, text="", font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR)

        button_1 = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=button_1, highlightthickness=0, command=self.right_ans)
        self.right_button.config(padx=20, pady=20)
        self.right_button.grid(column=0, row=3)

        button_2 = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=button_2, highlightthickness=0, command=self.wrong_ans)
        self.wrong_button.config(padx=20, pady=20)
        self.wrong_button.grid(column=1, row=3)

        self.score_label = Label(text=f"Score: {0}", fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score_label.config(padx=10, pady=5)
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.new_word, text=q_text)
        else:
            self.canvas.itemconfig(self.new_word,
                                   text="You've reached the questions limits of this quiz. Thanks for playing 😊")
            self.right_button.config(state="disable")
            self.wrong_button.config(state="disable")

    def right_ans(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_ans(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

