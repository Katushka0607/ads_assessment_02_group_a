"""
Simple Calculator
"""
# Provide your solution here

def calculate(num1: int, num2: int, operator: str):
    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            result = "Division by 0 is not allowed!"
        else:
            result = num1 / num2
    else:
        result = "Invalid operator!"
    return result



"""
Reverse Word
"""
# Provide your solution here

def reverse_word(word: str):
    index = len(word) - 1
    while index >= 0:
        if index == len(word) - 1:
            print(word[index].upper(), end="")
        else:
            print(word[index], end="")
        index -= 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

# Task 01:
number1 = int(input("Enter number 1: >> "))
number2 = int(input("Enter number 2: >> "))
operator_input = input("Enter operator (+,-,*,/): >> ")
print("Result: " + str(calculate(number1, number2, operator_input)))

# Task 02:
input_word = input("Please type in a word: >> ")
reverse_word(input_word)

