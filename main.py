from abc import ABC, abstractmethod


class AbsClass(ABC):
    @abstractmethod
    def accessData(self):
        pass


class GetJSON(AbsClass):
    def accessData(self):
        print("Data...")


class GetXML(AbsClass):
    def __init__(self, name):
        self.name = name

    def accessData(self):
        print("Data...")

    def __str__(self):
        return "I'm " + self.name


getter = GetXML("XML getter")
getter.accessData()
print(dir(GetXML))
print(GetXML.__class__)
print(type(GetXML))
print("*" * 11)
print(getter)
