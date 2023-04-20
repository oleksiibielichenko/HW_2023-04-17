from classes.classes import QA
from classes.classes import Developer
from classes.classes import Employee
import random

qa_1 = QA('Frank', '56')
qa_2 = QA('Mike', '42')
qa_3 = QA('Bob', '37')
dev_1 = Developer('John', '23')
dev_2 = Developer('Piter', '19')
dev_3 = Developer('Stefany', '26')

list_of_employee = [qa_1, qa_2, qa_3, dev_1, dev_2, dev_3]

i = random.randint(0, len(list_of_employee)-1)
dismissed_employee = list_of_employee[i]
print('Dismissed employee is', dismissed_employee.__dict__['name'])
dismissed_employee.unemployed = True
Employee.status(list_of_employee)
