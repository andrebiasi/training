class Adult:
    def __init__(self, name, height, weight, eye_color):
        self.name = name
        self.height = height
        self.weight = weight
        self.eye_color = eye_color

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.height, self.weight, self.eye_color)

    def print_name(self):
        print("Name is {}".format(self.name))


tom = Adult("Tom", 6, 150, "brown")
tom.print_name()


class Elderly(Adult):
    pass


class Kid(Adult):
    def print_name(self):
        super().print_name()
        print("Kid's name is: {}".format(self.name))

    def print_cartoon(self, fav_cartoon):
        print("Favourite cartoon is {}".format(fav_cartoon))


kid = Kid("Sam", 5, 75, "blue")
kid.print_name()
kid.print_cartoon("He-man")


class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


doggy = Dog("Max", "labrador", tom)
print(doggy.name)
print(doggy.breed)
print("The owner is {}".format(doggy.owner))


adult1 = Adult("Tom", 6, 150, "brown")
adult2 = adult1
print(adult1)
print(adult2)
adult2 = Adult("Bob", 5, 100, "blue")
print(adult1)
print(adult2)
print(adult1 is adult2)

print("*" * 30)
adult3 = Adult("Mike", 6, 150, "brown")
adult4 = adult3
print(adult3)
print(adult4)
adult4.name = "Ivan"
print(adult3)
print(adult4)
print(adult3 is adult4)
