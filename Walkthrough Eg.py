"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


STATE_NAMES = {"qld": "Queensland", "nsw": "New South Wales", "nt": "Northern Territory", "wa": "Western Australia",
               "act": "Australian Capital Territory", "vic": "Victoria", "tas": "Tasmania"}

# print(STATE_NAMES)
for key, value in STATE_NAMES.items():
    print('{:3} is {}'.format(key, value))




state = input("Enter short state: ")
state = state.lower()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")
    state = state.lower()
