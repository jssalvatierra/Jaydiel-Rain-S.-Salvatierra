#Jaydiel Rain S. Salvatierra
#8-Adelfa

Name = ""
Score1 = 0
Score2 = 0
Score3 = 0

def display_header():
    print("===================================")
    print("Student Performance Evaluator")
    print("===================================")
def display_student_info():
    name = input ("Enter Student Name: ")
    score1 = int(input("First assessment score: "))
    score2 = int(input("Second assessment score: "))
    score3 = int(input("Third assessment score: "))
    return name, score1, score2, score3
def evaluate_performance(score1, score2, score3):
    avg = (score1 + score2 + score3) / 3
    global avg

    if avg >= 90:
        Performance =  "Outstanding"
    if avg >= 85:
        Performance = "Very Satisfactory"
    if avg >= 80:
        Performance =  "Satisfactory"
    if avg >= 75:
        Performance =  "Fairly Satisfactory"
    else:
        Performance = "Needs improvement"


def display_report():
    print(f"Student Name: {Name}")
    print(f"Assessment scores: {Score1}, {Score2}, {Score3}")
    print(f"Average score: {avg}")
    print(f"Performance: {Performance}")



display_header()
display_student_info()
evaluate_performance()
display_report()
