class Exam:
    def __init__(self, answer_key):
        self.answer_key = answer_key
        self.student_responses = []
    
    def student_answer(self, response):
        self.student_responses.append(response)
    
    def correct_answers(self):
        correct_count = 0
        for i in range(len(self.student_responses)):
            if self.student_responses[i] == self.answer_key[i]:
                correct_count += 1
        return correct_count
    
    def score(self):
        total_score = 0
        for i in range(len(self.student_responses)):
            if i < 10:  
                if self.student_responses[i] == self.answer_key[i]:
                    total_score += 0.5
            else:  
                if self.student_responses[i] == self.answer_key[i]:
                    total_score += 1
        return total_score
    
    @staticmethod
    def highest_score(exam1, exam2):
        if exam1.correct_answers() > exam2.correct_answers():
            return exam1.score()
        elif exam2.correct_answers() > exam1.correct_answers():
            return exam2.score()
        else:
            return "Both students have the same number of correct answers"

class AnswerKey:
    def __init__(self, answers):
        self.answers = answers

answer_key = AnswerKey(["A", "B", "C", "D", "E", "A", "B", "C", "D", "E", "A", "B", "C", "D", "E"])
student1_exam = Exam(answer_key.answers)
student2_exam = Exam(answer_key.answers)

student1_exam.student_answer("A")
student1_exam.student_answer("B")

student2_exam.student_answer("A")
student2_exam.student_answer("C")

print("Student 1's score:", student1_exam.score())
print("Student 2's score:", student2_exam.score())

print("Student with the highest score:", Exam.highest_score(student1_exam, student2_exam))
