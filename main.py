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
        result = MyIterable(0).l
        result.l = self.l+other.l
        return result


a = MyIterable(10)
print(a[5])
for i in a:
    print(i)

a.addItem(12)

print(a[2:5])
print(a)
print(type(a))

print("-"*15)

print(len(a))

a()