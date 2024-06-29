"""Class average program with sentinel - controlled iteration. """


#initialization phase
total = 0  #sum of grades
grade_counter = 0  # sum of grades


#processing grade
grade = int(input('Enter grade, -1 to end: ')) #get one grade

while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: ')) #get one grade


#termination
if grade_counter != 0:
    average = total/grade_counter
    print(average)
else:
    print("No grades were entered")


for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()