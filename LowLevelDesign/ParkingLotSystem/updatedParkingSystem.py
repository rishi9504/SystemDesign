from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime
import threading
import uuid
import time

# Enums for Vehicle Types & Spot Status
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    TRUCK = "Truck"

class SpotStatus(Enum):
    OCCUPIED = "Occupied"
    AVAILABLE = "Available"

# Vehicle Classes
class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.CAR)

class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)

class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.TRUCK)

# Parking Spot Class
class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.status = SpotStatus.AVAILABLE
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        if self.status == SpotStatus.AVAILABLE and vehicle.vehicle_type == self.spot_type:
            self.vehicle = vehicle
            self.status = SpotStatus.OCCUPIED
            return True
        return False

    def release_spot(self):
        self.vehicle = None
        self.status = SpotStatus.AVAILABLE

# Parking Level Class
class ParkingLevel:
    def __init__(self, level_id, num_spots):
        self.level_id = level_id
        self.spots = [ParkingSpot(i, VehicleType.CAR if i % 3 == 1 else VehicleType.MOTORCYCLE if i % 3 == 2 else VehicleType.TRUCK) for i in range(num_spots)]
        self.lock = threading.Lock()

    def find_available_spot(self, vehicle_type):
        with self.lock:
            for spot in self.spots:
                if spot.status == SpotStatus.AVAILABLE and spot.spot_type == vehicle_type:
                    return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_available_spot(vehicle.vehicle_type)
        if spot:
            spot.assign_vehicle(vehicle)
            return spot.spot_id
        return None

    def release_spot(self, spot_id):
        with self.lock:
            for spot in self.spots:
                if spot.spot_id == spot_id:
                    spot.release_spot()
                    return True
        return False

# Parking Lot Class
class ParkingLot:
    def __init__(self, levels):
        self.levels = [ParkingLevel(i, 10) for i in range(levels)]
        self.lock = threading.Lock()

    def find_parking_spot(self, vehicle):
        with self.lock:
            for level in self.levels:
                spot_id = level.park_vehicle(vehicle)
                if spot_id is not None:
                    return level.level_id, spot_id
        return None, None

    def release_parking_spot(self, level_id, spot_id):
        with self.lock:
            return self.levels[level_id].release_spot(spot_id)

# Pricing Strategy (Strategy Pattern)
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, entry_time, exit_time, vehicle_type):
        pass

class FlatRatePricing(PricingStrategy):
    def __init__(self, rate_per_hour):
        self.rate_per_hour = rate_per_hour

    def calculate_price(self, entry_time, exit_time, vehicle_type):
        duration_hours = (exit_time - entry_time).total_seconds() / 3600
        return round(duration_hours * self.rate_per_hour, 2)

class PeakHourPricing(PricingStrategy):
    def __init__(self, base_rate, peak_rate):
        self.base_rate = base_rate
        self.peak_rate = peak_rate

    def calculate_price(self, entry_time, exit_time, vehicle_type):
        total_price = 0
        current_time = entry_time

        while current_time < exit_time:
            hour = current_time.hour
            total_price += self.peak_rate if 8 <= hour <= 10 or 17 <= hour <= 19 else self.base_rate
            current_time = current_time.replace(hour=current_time.hour + 1)

        return round(total_price, 2)

# Ticket Class
class Ticket:
    def __init__(self, vehicle, level_id, spot_id, pricing_strategy):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.level_id = level_id
        self.spot_id = spot_id
        self.entry_time = datetime.now()
        self.exit_time = None
        self.pricing_strategy = pricing_strategy
        self.total_cost = 0

    def process_exit(self):
        self.exit_time = datetime.now()
        self.total_cost = self.pricing_strategy.calculate_price(self.entry_time, self.exit_time, self.vehicle.vehicle_type)
        return self.total_cost

    def get_ticket_info(self):
        return {
            "ticket_id": self.ticket_id,
            "vehicle": self.vehicle.license_plate,
            "entry_time": self.entry_time.strftime("%Y-%m-%d %H:%M:%S"),
            "exit_time": self.exit_time.strftime("%Y-%m-%d %H:%M:%S") if self.exit_time else "In Parking",
            "total_cost": self.total_cost,
        }

# Exit Gate Processing
class ExitGate:
    def __init__(self, gate_id, parking_lot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot

    def process_exit(self, ticket):
        total_cost = ticket.process_exit()
        success = self.parking_lot.release_parking_spot(ticket.level_id, ticket.spot_id)
        if success:
            print(f"Vehicle {ticket.vehicle.license_plate} exited. Total charge: ${total_cost}")
            return True
        return False

# Simulation
if __name__ == "__main__":
    parking_lot = ParkingLot(3)
    entry_gate = ParkingLot(1)
    exit_gate = ExitGate(1, parking_lot)

    pricing_strategy = PeakHourPricing(base_rate=5, peak_rate=10)
    car = Car("CAR-123")
    car_ticket = Ticket(car, 1, 101, pricing_strategy)
    print("Car Ticket:", car_ticket.get_ticket_info())

    time.sleep(2)
    exit_gate.process_exit(car_ticket)
