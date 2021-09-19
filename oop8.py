class valorant:
    def __init__(self,name,id,rank,elo):
        self.name = name
        self.id = id
        self.rank = rank 
        self.elo = elo
    def win(self,value):
        for i in range(value):
            self.elo += 30
    def lose(self,value):
        for i in range(value):
            self.elo -= 28
    def rank_up(self):
        if self.elo <= 100:
            self.rank = "Iron"
        elif self.elo <= 300:
            self.rank = "Silver"
        elif self.elo <= 600:
            self.rank = "Gold"
        elif self.elo <= 900:
            self.rank = "Platinum"
        elif self.elo <= 1200:
            self.rank = "Daimond"
        elif self.elo <= 1500:
            self.rank = "Immortal"
        elif self.elo <= 1800:
            self.rank = "Radiant"
        else:
            self.rank = "Radiant"
    def __str__(self):
        return f"{self.name}{self.id} your current rank is {self.rank}"
name = input("IN GAME NAME: ")
id = input("ID TAG: ")
rank = input("Your Rank: ")
elo = int(input("Your Elo: "))
w = int(input("How many games you have won: "))
l = int(input("How many games you have lost: "))
s1 = valorant(name,id,rank,elo)
s1.win(w)
s1.lose(l)
s1.rank_up()
print(s1)