from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR="#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzy")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=400,height=300)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.ques=self.canvas.create_text(200,150,text="Question",font=("Arial",20,"italic"),width=350)
        
        Score=Label(text="Score: 3",bg=THEME_COLOR,fg="white",font=("Arial",10,"bold"),pady=20)
        Score.grid(row=0,column=1)
        
        rimg=PhotoImage(file="./QuizGame/img/true1.png")
        wimg=PhotoImage(file="./QuizGame/img/false2.png")
        
        true=Button(image=rimg,bg=THEME_COLOR)
        true.grid(row=2,column=1)
        
        false=Button(image=wimg,bg=THEME_COLOR)
        false.grid(row=2,column=0)
        
        self.next_ques()
        
        self.window.mainloop()
        
    def next_ques(self):
        self.canvas.itemconfig(self.ques,text=self.quiz.next_q())
        