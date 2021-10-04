class Library:
    def __init__(self,*args):
        self.lst = []
        for i in args:
            self.lst.append(i)
        
    def displayavailablebooks(self):
        print("List of available books")               #Library 
        for i in self.lst:
            print(i)
    def lendbooks(self,book):
        if book in self.lst:
            self.lst.remove(book)
            print("You lended the book. Please return the book in time.")
        else:
            print("Sorry the book is not availabe.")
    def addbooks(self,book):
        print("Thanks for returning the book.")
        self.lst.append(book)
class Customer:
    def reqbooks(self):
        self.book = input("Enter the name of the book you wanna borrow.")
        return self.book
    def returnbooks(self):
        self.book = input("The book you want to return.")
        return self.book



library = Library("The Outsider","Mind Games","Foe")
customer = Customer()
while True:
    print("Input 1 to display the available books.")
    print("Input 2 to request for a book.")
    print("Input 3 to return a book.")
    print("Input 4 to quit.")
    req = int(input())
    if req == 1:
        library.displayavailablebooks()
    elif req == 2:
        gg =customer.reqbooks()
        library.lendbooks(gg)
    elif req == 3:
        gg = customer.returnbooks()
        library.addbooks(gg)
    elif req == 4:
        quit()

