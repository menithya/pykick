class schoolmember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print 'name is %s \nand age is %s' %(self.name,self.age)
class Teacher(schoolmember):
    def __init__(self,salary,name,age):
        schoolmember.__init__(self,name,age)
        self.salary=salary

    def display(self):
        schoolmember.display(self)
        print "%s salary is %s" %(self.name,self.salary)
class Students(schoolmember):
    def __init__(self,name,age,marks):
        schoolmember.__init__(self,name,age)
        self.marks=marks
    def displyaMakrs(self):
        schoolmember.display(self)
        print "%s marks is %s" %(self.name,self.marks)


teacher =Teacher(100,"nithya",30)
teacher.display()
ram = Students("raj",10,80)
ram.displyaMakrs()
