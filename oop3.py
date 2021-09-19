class game:
    def __init__(self,name,playerbase,year):
        self.name = name
        self.playerbase = playerbase
        self.year = year
    def __eq__(self,object):
        return self.name == object.name and self.year == object.year
        
s1 = game("Valorant",2,2020)
s2 = game("Valorant",2,2020)
print(s1.playerbase) 
print(s1==s2)
        
  