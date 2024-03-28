class Employee:
    pass

emp_1=Employee()
emp_2=Employee()

print(emp_1)
print(emp_2)

emp_1.first=("Elone")
emp_1.last=("Altman")
emp_1.email=("Elonealtman@gmail.com")

emp_2.first=("Sam")
emp_2.last=("Mask")
emp_2.email=("SamMask#gmail.com")

print(emp_1.last)
print(emp_2.last)


#SAME IN DIFFRENT METHOD WITH init

class workers:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.gmail=first+last+'.'+"@gmail.com"
    def fullname(self):
         return'{}{}'.format(self.first,self.last)   
        
work_1=workers('Bill','skcar',45000)
work_2=workers('tom','kitty',35000)

print(work_1.gmail)
print(work_2.gmail)

# print('{} {}'.format(emp_1.first,emp_1.last))
print(work_1.fullname())



