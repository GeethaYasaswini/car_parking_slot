from parkinglot import ParkingLot
from car import Car
import random

def main():
    # Create a parking lot
    size=int(input())
    parking_lot = ParkingLot(size)

    # Create an array of cars with random license plates
    cars = [Car(f"{random.randint(1000000, 9999999)}") for _ in range(10)]

    # Simulate parking
    for car in cars:
        spot_number = random.randint(0, parking_lot.calculate_array_size() - 1)
        parked_spot = parking_lot.park_car(car, spot_number)
        if parked_spot is None:
            print(f"{car} unable to park in any spot.")

    # Save the mapping to a JSON file
    with open("parking_mapping.json", "w") as file:
        file.write(parking_lot.map_to_json())

if __name__ == "__main__":
    main()
