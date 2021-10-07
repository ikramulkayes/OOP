#Write your code here
class Shape:
    def __init__(self,dis,num1,num2):
        self.choice = dis
        self.num1 = num1
        self.num2 = num2
    def area(self):
        if self.choice == "Triange":
            final = self.num1 * self.num2 * 0.5
        elif self.choice == "Square":
            final = self.num1 * self.num2
        elif self.choice == "Rhombus":
            final = self.num1 * self.num2 * 0.5
        elif self.choice == "Rectangle":
            final = self.num1 * self.num2
        else:
            final = "Shape unknown"
        print("Area",final)
        
#Do not change the following code:
triangle_1 = Shape("Triangle",10,25)
triangle_1.area()
print("==========================")
square_1 = Shape("Square",10,10)
square_1.area()
print("==========================")
rhombus_1 = Shape("Rhombus",18,25)
rhombus_1.area()
print("==========================")
rectangle_1 = Shape("Rectangle",15,30)
rectangle_1.area()
print("==========================")
trapezium_1 = Shape("Trapezium",15,30)
trapezium_1.area()