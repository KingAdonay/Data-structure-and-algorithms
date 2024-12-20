def gradingStudents(grades):
    finalGrades = []
    for grade in grades:
        finalGrade = grade
        if grade > 35 and grade % 5 != 0:
            remainder = grade % 5
            if remainder >= 3:
                finalGrade = grade  + (5 - remainder)
        
        finalGrades.append(finalGrade)
    return finalGrades

# Tests below
def checkSolution(actual, expected):
    status = 'passed'
    for index, value in enumerate(expected):
        if actual[index] != value:
            status = 'failed'
            break
    
    return status

# Testcase 1: [73, 67, 38, 33]
expected = [75, 67, 40, 33]
result = gradingStudents([73, 67, 38, 33])
print(checkSolution(result, expected))

# Testcase 2: [20, 100, 36, 97, 98]
expected = [20, 100, 36, 97, 100]
result = gradingStudents([20, 100, 36, 97, 98])
print(checkSolution(result, expected))

