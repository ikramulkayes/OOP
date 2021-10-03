class instagram:
    def __init__(self,username,usertag):
        self.username = username
        self.usertag = usertag
        self.follower = 0
        self.following = 0
    def follow(self,user):
        user.follower += 1
        self.following += 1
kayes = instagram("Ikrarmul Kayes","kayes")
jack = instagram("Jacky Chan","jack")
kayes.follow(jack) #as the self means kayes and user is jack so as jack gets 1 follower and for kayes who is in self gets 1 for following
print(kayes.following)
print(jack.follower)
jack.follow(kayes)
print(kayes.follower)
print(jack.following)