def getNumber():
    a = 0
    while True:
        try:
            a = int(input("Enter a number: "))
        except:
            continue
        else:
            break

    return a


print(getNumber())
