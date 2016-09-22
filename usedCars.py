"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from Prac07.car import Car


def main():
    bus = Car(180, "Bus")
    bus.drive(30)

    limo = Car(100, "Limo")
    limo.add_fuel(20)
    limo.drive(115)
    # print("Limo fuel =", limo.fuel)
    #
    # print("Limo odo =", limo.odometer)
    #
    # print("fuel =", bus.fuel)
    # print("odo =", bus.odometer)

    print(limo)
    print(bus)

    # print("Car {}, {}".format(bus.fuel, bus.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=bus))

main()