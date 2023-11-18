class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
        
    def next_q(self):
        return f"Q.{self.question_number+1}: {(self.question_list[self.question_number]).text}"

    def correct_ans(self):
        return (self.question_list[self.question_number]).answer

    def check_ans(self,user_ans:str,correct_ans:str):
        if (user_ans==correct_ans):
            self.score+=1
            self.question_number+=1
            return True
        else:
            self.question_number+=1
            return False
            
    
    def still_has_questions(self):
        return self.question_number<len(self.question_list)
        