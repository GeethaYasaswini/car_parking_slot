import json

class ParkingLot:
    def __init__(self, square_footage):
        self.square_footage = square_footage
        self.parking_lot_array = [None] * self.calculate_array_size()

    def calculate_array_size(self):
        spot_size = 96
        return self.square_footage // spot_size

    def park_car(self, car, spot_number):
        initial_spot = spot_number
        while spot_number < len(self.parking_lot_array):
            if self.parking_lot_array[spot_number] is None:
                self.parking_lot_array[spot_number] = car
                print(f"{car} parked successfully in spot {spot_number}")
                break
            else:
                print(f"Spot {spot_number} is occupied. Trying another spot for car with license plate {car}")
                spot_number += 1
        else:
            print(f"No available spots for {car} at any spot. Parking lot is full.")

        # If the car parked successfully, return the spot number; otherwise, return None
        return spot_number if spot_number < len(self.parking_lot_array) else None

    def map_to_json(self):
        mapping = {f"Spot {i}": str(car) if car else None for i, car in enumerate(self.parking_lot_array)}
        return json.dumps(mapping, indent=2)