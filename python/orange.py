class Orange:
    print("Orange created")

    def __init__(self):
        self.color = "orange"
        self.weight = 10

    def __str__(self):
        return "Color: {}, Weight: {}".format(self.color, self.weight)

    def print_orange(self):
        print(self)
        print(self.color)
        print(self.weight)


my_orange = Orange()
my_orange.print_orange()


class Orange2:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight


my_orange = Orange2("dark orange", 20)
print(my_orange.color)
print(my_orange.weight)
