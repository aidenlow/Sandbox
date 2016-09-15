name = str(input("What is your string"))
count = {i:0 for i in "aeiouAEIOU"}
for character in name:
    if character in count:
        print(character, end="")