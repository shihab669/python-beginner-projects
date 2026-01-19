#we are creating a simple calculator for basic calculation

def calculation(n1, op, n2):
    if op == "+":
        result = (n1) + (n2)
    elif op == "-":
        result = (n1) - (n2)
    elif op == "*":
        result = (n1) * (n2)
    elif op == "/":
        result = (n1) / (n2)
    else:
        result = ""
        print("Invalid operator")

    return result
        

number1 = int(input("Enter first number: "))

operator = input("Select an operator (+, -, *, /): ").strip()
number2 = int(input("Enter secound number: "))
resultVar = calculation(number1, operator, number2)
print(resultVar)
