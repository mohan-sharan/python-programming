jack = {
  "name": "Jack",
  "homework": [92.0, 57.0, 77.0, 82.0],
  "quizzes": [99.0, 90.0, 94.0],
  "tests": [85.0, 97.0]
}
jones = {
  "name": "Jones",
  "homework": [10.0, 99.0, 98.0, 80.0],
  "quizzes": [86.0, 43.0, 99.0],
  "tests": [81.0, 67.0]
}
james = {
  "name": "James",
  "homework": [40.0, 0.0, 100.0, 100.0],
  "quizzes": [45.0, 65.0, 95.0],
  "tests": [100.0, 99.0]
}

student = [jack, jones, james]

def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  
  total = homework * .1 + quizzes * .3 + tests * .6
  return total

def get_letter_grade(score):
  if (score >= 90):
    return "A"
  elif (score >= 80):
    return "B"
  elif (score >= 70):
    return "C"
  elif (score >= 60):
    return "D"
  else:
    return "F"

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

print("CLASS AVERAGE:", get_class_average(student))

print("LETTER GRADE:", get_letter_grade(get_average(jack)))

print("AVERAGE:", get_average(jack))

'''
OUTPUT:
CLASS AVERAGE: 83.725
LETTER GRADE: A
AVERAGE: 90.6
'''
