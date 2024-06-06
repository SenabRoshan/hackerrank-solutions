# Challenge: Finding the percentage

# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input("Enter the number of students: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter a student's name to find the percentage: ")
    marks = student_marks.get(query_name)
    total = 0
    for x in marks:
        total = total + x
    
    average = total / len(marks)
    print(f"{average:.2f}")