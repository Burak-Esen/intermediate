class Dog:
    sound = "bark"

    def speak(self):
        print(Dog.sound)


class Cat:
    def __init__(self):
        self.sound = "Meeuw"

    def speak(self):
        print(self.sound)


d1 = Dog()
c1 = Cat()

c1.speak()
d1.speak()

c1.name = "Katz"
print(c1.name)
print(hasattr(c1, "surname"))
print(getattr(c1, "name"))
print(setattr(c1, "name", "Gerald"))
print(getattr(c1, "name"))
print(delattr(c1, "name"))
print(hasattr(c1, "name"))
