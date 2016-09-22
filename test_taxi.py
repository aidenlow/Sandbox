from Prac08.taxi import Car
from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi

def main():
    taxi1 = Taxi("Prius 1", 100)

    taxi1.start_fare()
    taxi1.drive(40)
    print("$", taxi1.get_fare())
    print(taxi1)
    taxi1.start_fare()
    taxi1.drive(100)
    print("$", taxi1.get_fare())
    print(taxi1)

    some_car = UnreliableCar("Nissan", 100, 99)
    some_car.drive(40)
    print(some_car)

    fancy_taxi = SilverServiceTaxi("Subaru", 100, 2)
    print(fancy_taxi.price_per_km)
    fancy_taxi.drive(10)
    print(fancy_taxi.get_fare())
    print(fancy_taxi)




main()