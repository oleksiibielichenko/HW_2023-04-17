from classes.classes import QA
from classes.classes import Developer
import random

qa_1 = QA('Frank', '56')
qa_2 = QA('Mike', '42')
qa_3 = QA('Bob', '37')
dev_1 = Developer('John', '23')
dev_2 = Developer('Piter', '19')
dev_3 = Developer('Stefany', '26')

list_of_employee = [qa_1, qa_2, qa_3, dev_1, dev_2, dev_3]

print(list_of_employee)
# random.randint(list_of_employee.index[0], len(list_of_employee))

# def quit(employee):
#     global list_of_employee
#     from
