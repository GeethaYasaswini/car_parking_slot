class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"Car with license plate {self.license_plate}"