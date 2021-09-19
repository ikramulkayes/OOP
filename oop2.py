class software:
    saul = "Better call me "      #class attribute
    def __init__(self,name,age,level,salary):
        self.name = name
        self.age = age             #intance attribute
        self.level = level
        self.salary = salary
    def __str__(self):
        information =f"Name = {self.name}  Age = {self.age}"
        return information
    def __eq__(self,other):
        return self.name == other.name and self.age == other.age
    def gg(age):
        if age > 28:
            return 7000
        else:
            return 4000





se1 = software("Jamal",28,"Junior",4000)
se2 = software("Jamal",28,"Junior",4000)
print(se1)
print(se1 == se2)
print(software.gg(29))