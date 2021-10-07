#Write your code here

class Calculator:
    def __init__(self,num1,num2,op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
    def calculate_button(self):
        if self.op == "+":
            return self.num1 + self.num2
        elif self.op == "-":
            return self.num1 - self.num2
        elif self.op == "*":
            return self.num1 * self.num2
        elif self.op == "/":
            return self.num1 / self.num2
    def details(self):
        if self.op == "+":
            print(self.num1, "+" ,self.num2,"=",self.num1 + self.num2)
        elif self.op == "-":
            print(self.num1, "-" ,self.num2,"=",self.num1 - self.num2)
        elif self.op == "*":
            print(self.num1, "*" ,self.num2,"=",self.num1 * self.num2)
        elif self.op == "/":
            print(self.num1, "/" ,self.num2,"=",self.num1 / self.num2)
        






# TODO

#Do not change the following code:
add = Calculator(10, 20, '+')
val = add.calculate_button()
print("Returned value:", val)
add.details()
print("==================")

sub = Calculator(val, 10, '-')
val = sub.calculate_button()
print("Returned value:", val)
sub.details()
print("==================")

div = Calculator(val, 5, '*')
val = div.calculate_button()
print("Returned value:", val)
div.details()
print("==================")

mult = Calculator(val, 16, '/')
val = mult.calculate_button()
print("Returned value:", val)
mult.details()
print("==================")