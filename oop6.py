class office:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._salary = None
        self._bugs = 0
    def code(self):
        self._bugs += 1
    def public(self):
        if self._bugs < 10:
            self._salary = 4000
        elif self._bugs<50:
            self._salary = 10000
        return self._salary
    def set_salary(self,value):
        self._salary = value
        

    
s1 = office("July",98)
for i in range(40):
    s1.code()
print(s1._bugs)
s1.set_salary(6000)
print(s1.public())