class Schoolmember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print 'name is %s \nand age is %s' %(self.name,self.age)
class Teacher(Schoolmember):
    def __init__(self,salary,name,age):
        Schoolmember.__init__(self,name,age)
        self.salary=salary

    def display(self):
        Schoolmember.display(self)
        print "%s salary is %s" %(self.name,self.salary)
class Students(Schoolmember):
    def __init__(self,name,age,marks):
        Schoolmember.__init__(self,name,age)
        self.marks=marks
    def displyaMakrs(self):
        Schoolmember.display(self)
        print "%s marks is %s" %(self.name,self.marks)


teacher =Teacher(100,"nithya",30)
teacher.display()
ram = Students("raj",10,80)
ram.displyaMakrs()
