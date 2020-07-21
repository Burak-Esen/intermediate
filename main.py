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


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A cat created")

    def talk(self):
        print("Meuuww")


d = Dog("Buddy")
c = Cat("Kitty")

c.talk()


# print(isinstance(d, Animal))
# print(isinstance(d, Dog))
# print(isinstance(d, object))
# print("*"*11)
# print(issubclass(Animal,Dog))
# print(issubclass(Dog,Animal))
# print(issubclass(Dog, object))
# print("*"*11)
# print(Dog.mro())
