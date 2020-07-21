class Calculator:
    def __init__(self, a, b):
        self.history=[]
        self.a = a
        self.b = b

    def add(self):
        self.history.append("+")
        return self.a + self.b

    def substrctn(self):
        self.history.append("-")
        return self.a - self.b

    def multiplctn(self):
        self.history.append("*")
        return self.a * self.b

    def division(self):
        self.history.append("/")
        return self.a / self.b
    def printHistory(self):
        print(self.history)
    def clearHistory(self):
        self.history.clear()
    def startCalculator(self):
        choice = 1
        while choice != 0:
            print("0. Exit")
            print("1. Add")
            print("2. Substraction")
            print("3. Multiplication")
            print("4. Division")
            choice = int(input("Enter choice:"))
            if choice == 1:
                print("Result: ", self.add())
            elif choice == 2:
                print("Result: ", self.substrctn())
            elif choice == 3:
                print("Result: ", self.multiplctn())
            elif choice == 4:
                print("Result: ", self.division())
            elif choice == 0:
                print("Exiting! ")
            else:
                print("Invalid Choice !")


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

obj = Calculator(a, b)

obj.startCalculator()

obj.printHistory()
obj.clearHistory()
obj.printHistory()
