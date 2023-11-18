from question_model import Question
from data import question_data
import html

question_bank=[]
for i in range(len(question_data)):
    question_bank.append(Question(html.unescape(question_data[i]["question"]),question_data[i]["correct_answer"]))
    
from quiz_brain import QuizBrain
q_b=QuizBrain(question_bank)
while(q_b.still_has_questions()):    
    q_b.next_q()
else:
    print("You've Completed the quiz")
    print(f"Your score is {q_b.score}/{q_b.question_number}")
