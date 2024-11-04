class Person(object):
    def __init__(self,id_number,name):
        self.id_number = id_number
        self.name = name
    def display(self):

        print(self.name)

        print(self.id_number)
class Employee(Person):
    def __init__(self,id_number,name,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,id_number)



a = Employee('Rahual',880812,200000,'Intern')


a.display()