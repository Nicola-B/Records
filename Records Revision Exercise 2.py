#Nicola Batty
#30/01/2015
#Records Revision Exercise 2

class student_mark:
    def __init__(self):
        self.name = None
        self.mark = None
        self.total_mark = None

def input_name_and_mark():
    mark_list = []
    for count in range(3):
        marks = student_mark()
        marks.name = input("Please input the students name: ")
        marks.mark = int(input("Please input there mark: "))
        marks.total_mark = int(input("Please input the total mark of the test: "))
        mark_list.append(marks)
    return mark_list

def display_name_and_mark(mark_list):
    print("_"*30)
    print("|{0:^20}|{1:^7}|".format("Name", "Marks"))
    print("_"*30)
    for marks in mark_list:
        print("|{0:<20}|{1:>3}/{2:<3}|".format(marks.name, marks.mark, marks.total_mark))
        print("_"*30)

def student_marks():
    mark_list = input_name_and_mark()
    display_name_and_mark(mark_list)
