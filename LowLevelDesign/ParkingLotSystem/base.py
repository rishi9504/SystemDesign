from enum import Enum
from threading import Lock

# Enum for Vehicle Types
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    TRUCK = "Truck"

# Enum for Parking Spot Status
class SpotStatus(Enum):
    OCCUPIED = "Occupied"
    AVAILABLE = "Available"

# Base Class for Vehicles
class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        """
        Constructor for Vehicle class. The Vehicle class is a base class for
        all types of vehicles that can be parked in the parking lot. 

        The constructor takes two parameters: the license plate number and the
        type of the vehicle.

        :param license_plate: License plate number of the vehicle
        :type license_plate: str
        :param vehicle_type: Type of the vehicle
        :type vehicle_type: VehicleType
        """
        self.license_plate = license_plate
        """
        License plate number of the vehicle
        """
        self.vehicle_type = vehicle_type
        """
        Type of the vehicle
        """

class Car(Vehicle):
    def __init__(self, license_plate):
        """
        Constructor for car class. Calls the super-class constructor
        and passes the license plate and VehicleType.car as arguments.

        :param license_plate: License plate of the vehicle
        :type license_plate: str
        """
        super().__init__(license_plate, VehicleType.CAR)

class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        """
        Constructor for Motorcycle class. Calls the super-class constructor
        and passes the license plate and VehicleType.MOTORCYCLE as arguments.

        :param license_plate: License plate of the vehicle
        :type license_plate: str
        """
        super().__init__(license_plate, VehicleType.MOTORCYCLE)

class Truck(Vehicle):
    def __init__(self, license_plate):
        """
        Constructor for Truck class. Calls the super-class constructor
        and passes the license plate and VehicleType.Truck as arguments.

        :param license_plate: License plate of the vehicle
        :type license_plate: str
        """
        super().__init__(license_plate, VehicleType.TRUCK)
