#Nicola Batty
#03/02/2015
#Recods Development Exercise 1

class student_mark:
    def __init__(self):
        self.name = None
        self.module1 = None
        self.module2 = None
        self.module3 = None
        self.module4 = None
        self.total = None

def calculate_total_marks(marks):
    total = marks.module1 + marks.module2 + marks.module3 + marks.module4
    return total

def input_data():
    student_list = []
    for count in range(5):
        marks = student_mark()
        marks.name = input("please input the name of the student: ")
        marks.module1 = int(input("please input the mark the student got for the first module: "))
        marks.module2 = int(input("please input the mark the student got for the second module: "))
        marks.module3 = int(input("please input the mark the student got for the third module: "))
        marks.module4 = int(input("please input the mark the student got for the forth module: "))
        marks.total = calculate_total_marks(marks)
        student_list.append(marks)
    return student_list

def display_data(student_list):
    print("_"*70)
    print("|{0:<20}|{1:<8}|{2:<8}|{3:<8}|{4:<8}|{5:<11}|".format("Student name","Module 1", "Module 2","Module 3", "Module 4", "total marks"))
    print("_"*70)
    for marks in student_list:
        print("|{0:<20}|{1:>8}|{2:>8}|{3:>8}|{4:>8}|{5:>11}|".format(marks.name, marks.module1, marks.module2, marks.module3, marks.module4, marks.total))
        print("_"*70)

def student_marks():
    student_list = input_data()
    display_data(student_list)
