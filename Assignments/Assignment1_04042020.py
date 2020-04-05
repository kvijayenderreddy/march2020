# 1. Write a python program to calculate the average of 3 numbers.
# Note: Take 3 numbers from user
# Example:
# User input:  2,3,4
# Output: 3
# ==============
def average(one, two, three):
    avg = (int(one) + int(two) + int(three)) / 3
    return avg

# first_number = (input("Enter first number:"))
# second_number = (input("Enter second number:"))
# third_number = (input("Enter third number:"))

# print(average(first_number, second_number, third_number))



# 2. Write a python program to convert Celsius to Fahrenheit
# Fahrenheit = 9.0/5.0 * Celsius + 32
# ============================
def celciusToFaranheit():
    celsius = int(input("Enter the celsius value to convert into Farenheit:\n"))
    return 9.0/5.0 * celsius + 32

# print(celciusToFaranheit())


# 3. Write a python program to convert Fahrenheit to Celsius
# Celsius = (Fahrenheit - 32) * 5.0/9.0
# =======================
def faranheitToCelcius():
    Fahrenheit = int(input("Enter the Farenheit value to convert to Celsius:\n"))
    return (Fahrenheit - 32) * 5.0/9.0

# print(celciusToFaranheit())



# 4. Write a python program to convert KM/H to MPH
# mph =  0.6214 * kmh
# ==========================
def kmphToMPH(kmph):
    return 0.6214 * kmph

print(kmphToMPH(input("Enter the KMPH value to convert into MPH")))


# 5. Write a function taking list of numbers as parameter and print each number to be Even or Odd
# Example:
# List = [1,4,5,2,7,4,9,12,43]
# 1 = Odd
# 4 = Even
# ..... and so on
def even_odd():
    list1 = [1, 4, 5, 2, 7, 4, 9, 12, 43]
    for i in list1:
        if (i%2==0):
            print ("The number ",i, "is even")
        else:
            print("The number ", i, "is odd")

# even_odd()

'''
Assignment2:
1. Create a function 'Calculate' which will take three input values as below, :and return the result
calculate(num1, num2, operation):
first - number1
second - number2
third - 
    operation: add, subtract, division, multiplication
    operation: +, -, /, *
'''