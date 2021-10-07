#Write your code here
class Student:
    def __init__(self,name,id,sub,grades):
        self.name = name
        self.id = id
        self.sub = sub
        self.grades = grades
        print(f"--------- Department:{self.sub}  ---------")
        print(f"Name: {self.name}, ID: {id}")
    def calculate_CGPA(self):
        sum = 0
        for i in self.grades:
            sum+= i
        self.sum = sum / len(self.grades)
        self.sum = round(self.sum,2)
        print("CGPA:",self.sum)
    def print_details(self):
        if self.sum >3.8 and self.sum < 4:
            print("Your academic standing is 'Highest Distinction'")
        elif self.sum >3.65 and self.sum < 3.79:
            print("Your academic standing is 'High Distinction'")
        elif self.sum >3.5 and self.sum < 3.64:
            print("Your academic standing is 'Distinction'")
        elif self.sum >2.0 and self.sum < 3.49:
            print("Your academic standing is 'Satisfactory'")
        else:
            print("You cannot graduate")








# TODO

#Do not change the following code:
s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
s1.print_details()

s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
s2.print_details()

s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
s3.print_details()