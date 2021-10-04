#inharitance
class maincompany:
    name = "NewAge Inc."
    year = "2020"
    def yearfoundedmessage(self):
        print("The company was founded in",self.year)
class subcompany(maincompany):
    def tree(self):
        print(self.name,"Company is the main company founded in",self.year)
var = subcompany()         #did not event make an object for maincompany class 
var.tree()             