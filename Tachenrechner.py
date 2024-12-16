def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


def calculator():
    cal = input(
        "Wählen Sie eine Operation (addieren : add, subtrahieren: sbr, multiplizieren: mult oder dividieren: div)?"
    )
    a = int(input("Gib ein zahl: "))
    b = int(input("Gib ei zweiter Zahl: "))
    if cal == "add":
        print(f" Addition: {add(a, b)}")
    elif cal == "sbr":
        print(f"Substraction: {substract(a, b)}")
    elif cal == "mult":
        print(f"Multiplication: {mult(a, b)}")
    elif cal == "div":
        if b != 0:
            print(f"Division: {div(a, b)}")
        else:
            print("Error!")
    else:
        print("choice invalid!")


zahl1 = int(input("Gib ein zahl: "))
zahl2 = int(input("Gib ei zweiter Zahl: "))

print(f" Addition: {add(zahl1, zahl2)}")
print(f"Substraction: {substract(zahl2, zahl2)}")
print(f"Multiplication: {mult(zahl1, zahl2)}")

if zahl2 != 0:
    print(f"Division: {div(zahl1, zahl2)}")
else:
    print("Error!")

calculator()
