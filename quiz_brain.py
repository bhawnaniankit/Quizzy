class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
        
    def next_q(self):
        return f"Q.{self.question_number+1}: {(self.question_list[self.question_number]).text}"

    def check_ans(self):
        # self.check_ans(user_ans,(self.question_list[self.question_number]).answer)
        pass
        
    def check_ans(self,user_ans,correct_ans):
        if (user_ans.lower()==correct_ans.lower()):
            print("You got it right!")
            self.score+=1
        else:
            print("That's Wrong.")
            print(f"The correct answer is {correct_ans}")
            
        self.question_number+=1
        print(f"Your score is {self.score}/{self.question_number}")
        print()
    
    def still_has_questions(self):
        return self.question_number<len(self.question_list)
        