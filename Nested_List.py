if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])
    students.sort(key=lambda x: (x[1], x[0]))
    scores = []
    for student in students:
        scores.append(student[0])
    
    lowestScore = min(scores)
    secondLowestScore = min(score for score in scores if score > lowestScore)
    
    secondLowestStudents = [student[1] for student in students if student[0] ==secondLowestScore]

    
    for student in sorted(secondLowestStudents):
        print(student)
