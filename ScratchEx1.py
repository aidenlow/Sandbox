def main():
    number_of_picks = int(input("How many quick picks?"))

    from random import randint

    a_set = set()
    while True:
        a_set.add(randint(1,45))
        if len(a_set) == 6:
            break
    lst = sorted(list(a_set))
    print(lst)

main()