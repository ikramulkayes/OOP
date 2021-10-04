class Engine:
    name = "unreal5"
    website = "www.unreal.com"
class Apple:
    name = "M1"
    location = "california"
    
class Macbook(Engine,Apple):
    def tree(self):
        print("website",self.website)
        print("location",self.location)
        print("Name:",self.name)  #because Engine is defined first so name unreal5 is showing in the function
laptop = Macbook()
laptop.tree()