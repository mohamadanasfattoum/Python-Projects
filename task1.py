# Calculator
# Input: User provides two numbers and selects an operation
# (addition, subtraction, multiplication, division).
# Output: The result of the chosen operation.
# Input values:
# Enter the first number: 5
# Enter the first number: 5
# Enter operation (+, -, *, /): +
# Enter the second number: 3
# Output value: Result: 8

firt_number = int(input('Press your firt_number: '))
enter_operation = input('Enter operation (+, -, *, /): ')
second_number = int(input('Press your second_number: '))
result = []

def calculator():
    if enter_operation == '+':
        addition = firt_number + second_number
        result.append(addition)
        print(result)

    elif enter_operation == '-':
        subtraction = firt_number - second_number
        result.append(subtraction)
        print(result)
    
    elif enter_operation == '*':
        multiplication = firt_number * second_number
        result.append(multiplication)
        print(result)

    elif enter_operation == '/':
        division = firt_number / second_number
        result.append(division)
        print(result)
  

calculator()