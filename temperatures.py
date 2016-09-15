"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()


def celcius_to_fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def fahrenheit_to_celcius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Celsius =", celsius)


while choice != "Q":
    if choice == "C":
        celcius_to_fahrenheit()
    elif choice == "F":
        fahrenheit_to_celcius()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")