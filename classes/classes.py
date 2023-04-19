class Employee:
    unemployed = False

    def __init__(self, name, age):
        self.name = name
        self.age = age


class QA(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Developer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
