from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR="#375362"


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzy")
        self.WINDOW_TIMER=self.window.after(1000)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=400,height=300)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.ques=self.canvas.create_text(200,150,text="Question",font=("Arial",20,"italic"),width=350)
        
        self.Score=Label(text=f"Score: {self.quiz.score}",bg=THEME_COLOR,fg="white",font=("Arial",10,"bold"),pady=20)
        self.Score.grid(row=0,column=1)
        
        rimg=PhotoImage(file="./QuizGame/img/true1.png")
        wimg=PhotoImage(file="./QuizGame/img/false2.png")
        
        true=Button(image=rimg,bg=THEME_COLOR,command=self.usr_true)
        true.grid(row=2,column=1)
        
        false=Button(image=wimg,bg=THEME_COLOR,command=self.usr_false)
        false.grid(row=2,column=0)
        
        self.next_ques()
        
        self.window.mainloop()
        
    def next_ques(self):
        self.canvas.itemconfig(self.ques,text=self.quiz.next_q())
        
    def usr_true(self):
        if(self.quiz.question_number<=9):
            cond=self.quiz.check_ans("True",self.quiz.correct_ans())
            self.update_score()
        
        self.feedback(cond)
        
    def usr_false(self):
        if(self.quiz.question_number<=9):
            cond=self.quiz.check_ans("False",self.quiz.correct_ans())
            self.update_score()
        self.feedback(cond)
        
        
            
    def update_score(self):
        self.Score.config(text=f"Score: {self.quiz.score}")
        
    def feedback(self,cond):
        if cond:
            self.canvas.config(bg="green")
            WINDOW_TIMER=self.window.after(1000,self.go_back)
        else:
            self.canvas.config(bg="red")
            WINDOW_TIMER=self.window.after(1000,self.go_back)
            
    def go_back(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.next_ques()