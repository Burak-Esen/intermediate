class Calculator:
    operations = ["/", "*", "-", "+"]

    def __init__(self):
        self.history = [0]
        self.operationHistory =[]

    def add(self, number):
        res = number + self.history[-1]
        self.history.append(res)
        self.operationHistory.append("+")
        return res

    def subtract(self, number):
        res = self.history[-1] - number
        self.history.append(res)
        return res

    def multiply(self, number):
        res = self.history[-1] * number
        self.history.append(res)
        return res

    def divide(self, number):
        res = self.history[-1] / number
        self.history.append(res)
        return res

    def ac(self):
        self.history.clear()

    def startCalculator(self):
        print("Enter a number")
        self.history.append(int(input("Number: ")))
        print("And then another one with an operation prefix like +5 and so on...")
        while True:
            text = input("Enter another number")
            if text == "exit":
                break
            operation = text[0]
            if operation not in Calculator.operations:
                continue
            number = int(text[1:])
