class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.__hunger = hunger

    def express(self):
        if self.__hunger > 5:
            print("Moooooooooowwwwwwwwww")
        else:
            print("Moooww")


molly = Cow(500, 10)
print(molly.weight)
print(molly.__hunger)
molly.express()
