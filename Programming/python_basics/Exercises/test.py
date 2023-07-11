# Exercises # 1


'''def count_sheep():
    number = int(input("Counting sheeps: "))
    sheep = 0

    for number in range(number):
        print(number, "sheep")
    number += 1
    if number < 0:
        print("Enter a whole number")


count_sheep()def count_sheep():
    number = int(input("Counting sheeps: "))
    sheep = 0

    for number in range(number):
        print(number, "sheep")
    number += 1
    if number < 0:
        print("Enter a whole number")


count_sheep()'''

completed_projects = int(input("Enter number of completed projects: "))
exam_grade = int(input("Enter your result exam: "))

def final_grade():
    if completed_projects > 10 or exam_grade > 90:
        print("Your result is : 100")
    elif completed_projects > 5 and exam_grade > 75:
        print("Your result is : 90")
    elif completed_projects >= 2 and exam_grade > 50:
        print("Your result is : 75")
    else:
        print("Your result is : 0")

final_grade()

