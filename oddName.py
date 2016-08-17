"""Aiden Low"""
def main():
    name = str(input("What is you first name"))
    length_of_name = len(name)

    while length_of_name < 1:
        print("Invalid Name")
        name = str(input("What is you first name"))
        length_of_name = len(name)

    sliced = name[::2]
    print(sliced)

main()