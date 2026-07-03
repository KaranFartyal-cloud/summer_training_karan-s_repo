tillNow = 0
a = int(input("enter a number"))

c = input("enter the operator")

b = int(input("enter another number"))

if c == "*":
    tillNow = a * b

elif c == "+":
    tillNow = a + b

elif c == "-":
    tillNow = a - b
elif c == "/":
    tillNow = a / b
elif c == "//":
    tillNow = a // b
elif c == "%":
    tillNow = a % b
elif c == "==":
    tillNow = a == b
else:
    print("wrong operator or number")

print("answer is tillNow: ", tillNow)

while True:
    temp = int(input(("enter next number anything else will exit the program: ")))

    op  = input("enter the operator: ")

    if op == "*":
        temp *= tillNow
    elif op == "+":
        temp += tillNow

    elif op == "-":
        temp = tillNow - temp

    elif op == "/":
        temp = tillNow / temp
    elif op == "//":
        temp = tillNow // temp
    elif op == "%":
        temp = tillNow % temp
    elif op == "==":
        temp = tillNow == temp
    else:
        print("invalid input program is exiting")
    print(f"answer till now is {temp}")
    tillNow = temp
