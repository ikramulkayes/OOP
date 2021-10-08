class Animal:
    def __init__(self):
        self.eyes = 2

    def breath(self):
        print("On air!")
class Fish(Animal):

    def breath(self):
        super().breath
        print("On water!")       #defining new function
k = Fish()
k.breath()