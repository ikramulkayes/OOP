class tup:
    def __init__(self,*args):
        self.lst = []
        if len(args) < 5:
            for i in args:
                self.lst.append(i)  #it returns the last 5 items 
        else:
            count = len(args) - 5

            self.lst = args[count::]
    def reveal(self):
        return(list(self.lst))
var = tup("ruby","scarlet","gold","jazz","saphire","radiant","kohinur")
print(var.reveal())
