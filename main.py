from Math import aritmetic_functions

class MyIterable:
    def __init__(self, number):
        self.l = [i for i in range(number)]

    def __setitem__(self, key, value):
        self.l[key] = value

    def __getitem__(self, index):
        return self.l[index]

    def addItem(self, x):
        self = self.l.append(x)

    def __str__(self):
        return str(self.l)

    def __repr__(self):
        return "repr: " + str(self.l)

    def __len__(self):
        return len(self.l)

    def __call__(self):
        print("I'm a MyIterable object")

    def __add__(self, other):
        result = MyIterable(0)
        result.l = self.l + other.l
        return result

    def __gt__(self, other):
        return sum(self.l) > sum(other.l)

a = MyIterable(10)
b = MyIterable(5)
print(a+b)
try:
    print(b>=a)
except:
    print("An error occurred.")
else:
    print("Else Block")


if __name__=="__main__":
    print("I'm Main")
