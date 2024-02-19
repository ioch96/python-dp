class Cow:
    def __init__(self, weight, hunger):
        self.weight = weight
        self.hunger = hunger

    def express(self):
        if self.hunger > 5:
            print("Moooooooooowwwwwwwwww")
        else:
            print("Moooww")


molly = Cow(500, 10)
molly.express()
