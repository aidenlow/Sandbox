from Prac07.guitar import Guitar

BLANK = ''


def main():
    my_guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

    guitar_name = input("Name:")
    while guitar_name != BLANK:
        guitar_year = int(input("Year:"))
        guitar_cost = float(input("Cost:"))
        my_guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print('{} ({}) : ${} added'.format(guitar_name, guitar_year, guitar_cost))
        guitar_name = input("Name:")

    for i, guitar in enumerate(my_guitars):
        if guitar.is_vintage():
            vintage = "Vintage"
        else:
            vintage = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage))


main()
