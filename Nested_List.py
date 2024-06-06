# Challenge : Nested List

# Question :

#Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

#Explanation :

#There are  students in this class whose names and grades are assembled to build the following list:

#python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#The lowest grade of 37.21  belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    students = []
    for _ in range(int(input("Enter number of Students:"))):
        name = input("Name: ")
        score = float(input("Score: "))
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
