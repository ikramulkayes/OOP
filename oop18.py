#Write your code here
class Patient:
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        
    def print_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Weight",self.weight)
        print("Height",self.height)
        self.height = self.height/100
        self.bmi = self.weight/(self.height*self.height)
        print("BMI:",self.bmi)






# TODO

# Do not change the following code:
p1 = Patient("A", 55, 63.0, 158.0)
p1.print_details()
print()
p2 = Patient("B", 53, 61.0, 149.0)
p2.print_details()