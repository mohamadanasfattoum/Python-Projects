# Calculator
# Input: User provides two numbers and selects an operation
# (addition, subtraction, multiplication, division, Squared).
# Output: The result of the chosen operation.
# Input values:
# Enter the first number: 5
# Enter the first number: 5
# Enter operation (+, -, *, /,**): +
# Enter the second number: 3
# Output value: Result: 8


class Calculator:
    def __init__(self):
        while True:
            self.result = []
            choice = int(input('Press 0- to exit\nPress 1- to (+,-,*,/)\nperrs 2- to Squared number **2 \npress :  '))
            if choice == 1:
                self.calculator()

            elif choice == 2:
                self.squared()
            elif choice ==0:
                print('....Exit....')
                break


            end_choice = int(input('Press 0- to exit or 3- to Calculator: '))
            if end_choice == 0:
                print('....Exit....')
                break

            elif end_choice == 3:
                continue
                           
    def calculator(self):
        enter_operation = input('Enter operation (+, -, *, /): ')
        firt_number = int(input('Press your firt_number: '))
        second_number = int(input('Press your second_number: '))
        if enter_operation == '+':
            addition = firt_number + second_number
            self.result.append(addition)
            print(self.result)

        elif enter_operation == '-':
            subtraction = firt_number - second_number
            self.result.append(subtraction)
            print(self.result)
        
        elif enter_operation == '*':
            multiplication = firt_number * second_number
            self.result.append(multiplication)
            print(self.result)

        elif enter_operation == '/':
            division = firt_number / second_number
            self.result.append(division)
            print(self.result)

    def squared(self):
        squared_number = int(input('Press your squared_number: '))    
        squared_r = squared_number ** 2 
        self.result.append(squared_r)
        print(self.result)    

a=Calculator()