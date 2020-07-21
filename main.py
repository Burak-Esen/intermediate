class Animal:
    def __init__(self, name):
        self.name = name
        print("An animal created")

    def talk(self):
        print("An animal talking")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A dog created")

    def talk(self):
        print("Bark Bark")


d = Dog("Buddy")
print(d.name)
d.talk()
