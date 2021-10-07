#Write your code here
class Course:
    def __init__(self,name,faculty,section):
        self.name = name
        self.faculty = faculty
        self.section = section
    def detail(self):
        print(self.name+" - " +self.faculty+" - "+str(self.section))
    





# TODO

#Do not change the following code:
c1 = Course("CSE110", "TBA", 8)
c1.detail()
print("===============")
c2 = Course("CSE422", "MZP", 9)
c2.detail()