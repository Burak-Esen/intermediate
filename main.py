class MyIterable:
    def __init__(self, number):
        self.l = [i for i in range(number)]

    def __setitem__(self, key, value):
        self.l[key] = value

    def __getitem__(self, index):
        return self.l[index]


a = MyIterable(10)
print(a[5])
for i in a:
    print(i)
