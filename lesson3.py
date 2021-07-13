import os

def function_input(result = None):

    if result != None:
        number1 = result
    else:
        number1 = None
        while number1 == None or not float(number1):
            try:
                number1 = float(input("number1: "))
            except ValueError:
                print("Choose correct number: ")
    operator = None
    operators = ["+", "-" , "/" , "*", "**"]
    while operator == None or operator not in operators:
        try:
            operator = input("Operator: ")
            if operator not in operators:
                raise ValueError
        except ValueError:
            print("+", "-" , "/" , "*", "**")
    number2 = None
    while number2 == None or not float(number2):
        try:
            number2 = float(input("number2: "))
        except ValueError:
            print("Choose correct number 2: ")


    return number1, operator, number2

def function_operator(number1, operator, number2):
        if operator == '+':
            result = (number1 + number2)
        elif operator == '-':
            result = (number1 - number2)
        elif operator == '/':
            result = (number1 / number2)
        elif operator == '*':
            result = (number1 * number2)
        elif operator == '**':
            result = (number1 ** number2)
        else:
            return
        return result

result = None

while True:
    number1, operator, number2 = function_input(result)
    result = function_operator(number1, operator, number2)
    os.system("clear")
    print(result)


    # function_input()
    # function_operator()
    # function_input()
    #     if input("finish")
    #         break




# num1 = function_input()
# oper = function_operator()
# num2 = function_input()


# def function_operator (smth = "smth :"):
#     try:
#         opp = input(smth)
#         print(opp)
#
#         if smth == '+':
#             print(x + y)
#         elif smth == '-':
#             print(x - y)
#         elif smth == '*':
#             print(x * y)
#         elif smth == '/':
#             print(x / y)
#         else:
#             print('non')
#     return

#def function_operator()