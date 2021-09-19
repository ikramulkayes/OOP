class school:
    def __init__(self,name,student_id,sub):
        self.name = name
        self.student_id = student_id
        self.sub = sub
    def __str__(self):
        return f"Student Name = {self.name} Student ID = {self.student_id}"
s1 = school("Jamal Rahman",2322342,"CSE")
print(s1)
        