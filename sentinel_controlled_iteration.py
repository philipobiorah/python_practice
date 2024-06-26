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


