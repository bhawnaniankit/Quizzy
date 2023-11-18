from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html
from ui import QuizInterface

question_bank=[]
for i in range(len(question_data)):
    question_bank.append(Question(html.unescape(question_data[i]["question"]),question_data[i]["correct_answer"]))
    
    
q_b=QuizBrain(question_bank)
QuizUi=QuizInterface(q_b)    
# while(q_b.still_has_questions()):    
#     q_b.next_q()
# else:
#     print("You've Completed the quiz")
#     print(f"Your score is {q_b.score}/{q_b.question_number}")
