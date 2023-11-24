# car_parking_slot
# Parking Lot Simulation

This project is a simple parking lot simulation that emulates the process of cars attempting to park in available spots. It is implemented in Python and includes two main classes: `Car` and `ParkingLot`. The simulation is driven by a main script, `main.py`, which creates a parking lot, generates an array of cars with random license plates, and attempts to park them in random spots within the parking lot.

## Project Overview

### Car Class

The `Car` class represents a vehicle with a 7-digit license plate. It includes a magic method (`_str_`) to convert the class instance to a string, displaying the license plate.

### ParkingLot Class

The `ParkingLot` class represents the parking facility. It takes the square footage as input, calculates the array size based on the size of parking spots (assumed to be 8x12, 96 ft² per spot), and creates an array to represent the parking lot. The class also features a method to park a car, considering spot availability and handling cases where spots are already occupied. Additionally, there is an optional method to map vehicles to parked spots in a JSON object.

### Main Script (main.py)

The `main.py` script serves as the entry point for the simulation. It creates an instance of the `ParkingLot` class, generates an array of cars with random license plates, and attempts to park them in the parking lot. The script outputs messages indicating whether the parking was successful or not.
