"""Aiden Low"""
def main():
    name = get_name()

    sliced = name[::2]
    print(sliced)


def get_name():
    name = str(input("What is you first name"))
    length_of_name = len(name)
    while length_of_name < 1:
        print("Invalid Name")
        name = str(input("What is you first name"))
        length_of_name = len(name)
    return name


main()