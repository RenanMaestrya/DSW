class QuestionAnswer:
    def __init__(self, answer_key):
        self.answer_key = answer_key
    
    def answer_question(self, question_number):
        if question_number in self.answer_key:
            return self.answer_key[question_number]
        else:
            return "Question not found in the answer key"


answer_key = {
    1: "A",
    2: "B",
    3: "C",
}

qa = QuestionAnswer(answer_key)
question_number = 2
correct_answer = qa.answer_question(question_number)
print(f"Correct answer for question {question_number}: {correct_answer}")