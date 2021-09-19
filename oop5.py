class employe:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def work(self):
        print("GG")


class software(employe):
    def __init__(self, name, age, salary,level):
        super().__init__(name, age, salary)
        self.level = level
    def work(self):
        print(f"{self.name} is coding")
    

class designer(employe):
    def work(self):
        print(f"{self.name} is drawing")
    
s1 = software("Kamal",59,7600,"Experienced")
d1 = designer("James",21,3500)
print(s1.name,s1.salary)
s1.work()
d1.work()

