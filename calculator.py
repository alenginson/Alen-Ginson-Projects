def my_number(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

print("Enter First number")
num1 = int(input("num1: "))
print("Enter operation (+, -, *, /):")
operation = input().strip()  # strip removes any leading/trailing whitespace
print("Enter Second number")
num2 = int(input("num2: "))

result = my_number(num1, num2, operation)
print("Result:", result)