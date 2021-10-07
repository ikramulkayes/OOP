#Write your code here
class Vehicle:
    def __init__(self,name,speed,milage):
        self.name = name
        self.name = speed
        self.milage = milage
    def seating_capacity(self):
        self.seat = 50
        return(f"The seating capacity of a bus is {self.seat} passengers")
    def fare(self):
        sum = self.seat*100
        sum = sum + sum*0.1
        return(sum)




# TODO

#Do not change the following code:
School_bus = Vehicle("School Volvo", 180, 12)
print(School_bus.seating_capacity())
print("Total Bus fare is:", School_bus.fare())
