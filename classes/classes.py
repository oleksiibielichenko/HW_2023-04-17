class Employee:
    def __init__(self, name, age, unemployed=False):
        self.name = name
        self.age = age
        self.unemployed = unemployed

    @staticmethod
    def status(employees):
        for j in employees:
            print(j.__dict__)


class QA(Employee):
    def __init__(self, name, age, unemployed=False):
        super().__init__(name, age, unemployed)


class Developer(Employee):
    def __init__(self, name, age, unemployed=False):
        super().__init__(name, age, unemployed)
