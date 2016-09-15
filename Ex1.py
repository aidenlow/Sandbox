COLOUR_NAMES = {"aliceblue": "fof8ff", "aquamarine1": "7fffd4", "blue1": "0000ff", "brown": "a52a2a", "blueviolet": "8a2be2"}

colour = input("Enter colour name: ")
colour = colour.lower()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")
    colour = colour.lower()
