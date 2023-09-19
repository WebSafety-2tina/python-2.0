class employee:"所以员工基类"
empcount=0
def _int_(self,name,salary):
    self.name=name
    self.salary=salary
    employee.empcount+=1
def dispplaycount(self):
    print("Totai employee %d"% employee.empcount)
def displayemployee(self):
    print("Name:",self.name,"salary:",self.salary)
class test:
    def prt(self):
        print(self)
        print(self.__class__)
t=test()
t.prt()