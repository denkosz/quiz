from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    quest_text = i["question"]
    quest_answer = i["correct_answer"]
    new_quest = Question(quest_text, quest_answer)
    question_bank.append(new_quest)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_quest()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")