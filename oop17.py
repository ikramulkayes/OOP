class Student:
    def begin(self):
        self.skill = "beginner"
    def show(self):
        print("Level of skill is",self.skill)
class Hstudent(Student):
    def begin(self):
        self.skill = "Amature"
    def reset(self):
        super().begin()       #return the value to base class value



human = Hstudent()
human.begin()
human.show()
human.reset()
human.show()