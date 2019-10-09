def calculator(operator, x, y):
    if operator == "+":
        outcome = x + y
    elif operator == "-":
        outcome = x - y
    elif operator == "*":
        outcome = x * y
    elif operator == "/":
        outcome = x / y
    else:
        outcome = "Please enter a valid operator: +, -, *, /"

    return outcome
def main():
    operator = input("\nWhat is the operation you'd like to perform? ")
    num1 = float(input("\nWhat is your first number? "))
    num2 = float(input("\nWhat is your second number? "))

    result = calculator(operator, num1, num2)

    print(f"{num1} {operator} {num2} = {result}")
main()