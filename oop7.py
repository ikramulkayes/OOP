class anaconda:
    def __init__(self,name,id,rank,elo):
        self.name = name
        self.rank = rank
        self.id = id
        self.elo = elo
    def rankelo(self):
        self.elo += 10
    def rankup(self):
        if self.elo <=100:
            self.rank = "Iron"
        elif self.elo <= 200:
            self.rank = "Silver"
        elif self.elo <= 300:
            self.rank = "Gold"
        elif self.elo <= 400:
            self.rank = "Plat"
        else:
            self.rank = "Radiant"
        return self.rank
    def define(self,value):
        self.rank = value
    def message(self,new_rank):
        return f"You have been promoted to {new_rank} "
    def __str__(self):
        return f"{self.name}#{self.id} your current rank is {self.rank} and your elo is {self.elo}"
s1 = anaconda("Low_Fps","GOT","Iron",40)
for i in range(30):
    s1.rankelo()
print(s1.rankup())
#s1.define("Silver")
#print(s1.rank)
k = s1.rankup()
print(s1.message(k))
print(s1)

        