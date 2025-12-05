import data, question_model, quiz_brain

list_q = data.question_data
question_bank = []


for q in list_q:
    text = q["question"]
    answer = q["correct_answer"]
    import_q = question_model.Question(text, answer)
    question_bank.append(import_q)

initialize = quiz_brain.QuizBrain(question_bank)

while initialize.still_has_questions():
    initialize.next_question()

print(f"You have completed the quiz\nYour final score is: {initialize.score}/{len(question_bank)}")