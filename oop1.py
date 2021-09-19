se1 = ["Software engineer","Jamal",28,"Junior",4000]           #NO NEEEEEEEEEEEEEED
se2 = ["Software engineer","Sasha",30,"Senior",6000]

class software:
    saul = "Better call me "      #class attribute
    def __init__(self,name,age,level,salary):
        self.name = name
        self.age = age             #intance attribute
        self.level = level
        self.salary = salary
    def code(self,laguage):
        print( f"{self.name} is coding in {laguage}")
    def info(self):
        information = f"Name = {self.name}  Age = {self.age}"
        return information

se1 = software("Jamal",28,"Junior",4000)         #instance
print(se1.name,se1.salary,se1.saul)
print(software.saul)


se1.code("Python")
print(se1.info())

