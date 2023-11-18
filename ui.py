from tkinter import *
THEME_COLOR="#375362"

class QuizInterface:
    def __init__(self):
        self.window=Tk()
        self.window.title("Quizzy")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=260,height=260)
        self.canvas.grid(row=0,column=0,columnspan=2)
        self.ques=self.canvas.create_text(130,130,text="Question",font=("Arial",20,"normal"))
        
        rimg=PhotoImage(file="./QuizGame/img/right.png")
        wimg=PhotoImage(file="./QuizGame/img/wrong.png")
        
        right=Button(image=rimg)
        right.grid(row=1,column=1)
        
        wrong=Button(image=wimg)
        wrong.grid(row=1,column=0)
        
        self.window.mainloop()
        
    def change_ques(self,string):
        self.canvas.itemconfig(self.ques,text=string)
        
if __name__=="__main__":
    QuizUi=QuizInterface()
    QuizUi.change_ques("helloo")