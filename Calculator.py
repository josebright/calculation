import math
print('A simple scientific calculator')
print('What calculation do you need')
def Add(x, y):
    return x + y
def Sub(x, y):
    return x - y
def Mul(x, y):
    return x * y
def Div(x, y):
    return x // y
def Mod(x, y):
    return x % y
def Exp(x, y):
    return x ** y
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)
def log(x):
    return math.log10(x)
print("For arithmetic calculation, enter 1:" + "\n" + "For angles calculation enter 2:" + "\n" "Calculation of plane shapes enter 3:")
number = input()
if number == "1":
    print("Add enter 1:" + "\n" + "Sub enter 2:" + "\n" + "Mul enter 3:" + "\n" + "Div enter 4:" + "\n" + "Mod enter 5:" + "\n" + "Exp enter 6:")
    choice = input()
    x = int(str(input("Enter your first number ")))
    y = int(str(input("Enter your second number ")))
    if choice == "1":
        print(x, "+", y, "=", Add(x, y))
    elif choice == "2":
        print(x, "-", y, "=", Sub(x, y))
    elif choice == "3":
        print(x, "*", y, "=", Mul(x, y))
    elif choice == "4":
        print(x, "//", y, "=", Div(x, y))
    elif choice == "5":
        print(x, "%", y, "=", Mod(x, y))
    elif choice == "6":
        print(x, "**", y, "=", Exp(x, y))
    else:
        print("syntax error")
elif number == "2":
    print("sin enter 1:" + "\n" + "cos enter 2:" + "\n" + "tan enter 3:")
    choice = input()
    if choice == "1":
        x = int(str(input("Enter the angle ")))
        Sine = math.cos(x / 360.0 * 2 * math.pi)
        print("Ans = " + str(math.sin(x)))
    elif choice == "2":
        ang = int(str(input("Enter the angle ")))
        cos = math.cos(ang / 360.0 * 2 * math.pi)
        print(cos)
    elif choice == "3":
        ang = int(str(input("Enter the angle ")))
        tan = math.tan(ang / 360.0 * 2 * math.pi)
        print(tan)
    else:
        print("syntax error")
elif number == "3":
    print("For area of shapes enter 1:" + "\n" + "For perimeter of shapes enter 2:")
    choice = input()
    if choice == "1":
        print("area of triangle enter 1:" + "\n" + "area of circle enter 2:")
        choice = input()
        if choice == "1":
            h = int(str(input("Enter the height")))
            b = int(str(input("Enter the base")))
            area = 1/2 * b * h
            print(area)
        elif choice == "2":
            r = int(str(input("Enter the radius:")))
            area = 22/7 * r ** 2
            print("Ans = " + str(area))
        else:
            print("syntax error")
    elif choice == "2":
        print("perimeter of a circle enter 1:" + "\n" + "perimeter of a rectangle enter 2:")
        choice == input()
        if choice == "1":
            r = int(str(input("Enter the radius:")))
            perimeter = 2 * 22 / 7 * r
            print("Ans = " + perimeter)
        elif choice == "2":
            L = int(str(input("Enter the length:")))
            B = int(str(input("Enter the breath:")))
            perimeter = 2 * (L + B)
            print("Ans = " + perimeter)
        else:
            print("syntax error")
    else:
        print("syntax error")
else:
    print("syntax error")
exit = input('PRESS ENTER TO EXIT')