#Nicola Batty
#30/01/2015
#Records Rivision Exercise 1

class student_mark:
    def __init__(self):
        self.name = None
        self.mark = None
        self.total_mark = None

def input_name_and_mark():
    marks = student_mark()
    marks.name = input("Please input the students name: ")
    marks.mark = int(input("Please input there mark: "))
    marks.total_mark = int(input("Please input the total mark of the test: "))
    return marks

def display_name_and_mark(marks):
    print("{0} got {1}/{2}".format(marks.name, marks.mark, marks.total_mark))

def student_marks():
    marks = input_name_and_mark()
    display_name_and_mark(marks)
