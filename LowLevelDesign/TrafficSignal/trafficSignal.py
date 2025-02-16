from enum import Enum
from typing import List, Dict
import time
from abc import ABC, abstractmethod

# Define the possible signal states
class SignalState(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"

# Define different types of vehicles for emergency handling
class VehicleType(Enum):
    REGULAR = "REGULAR"
    AMBULANCE = "AMBULANCE"
    FIRE_TRUCK = "FIRE_TRUCK"
    POLICE = "POLICE"

# Interface for traffic detection
class TrafficDetector(ABC):
    @abstractmethod
    def detect_emergency_vehicle(self) -> bool:
        pass
    
    @abstractmethod
    def get_traffic_density(self) -> float:
        pass

# Concrete implementation of traffic detector
class SensorBasedTrafficDetector(TrafficDetector):
    def __init__(self):
        self.emergency_vehicle_present = False
        self.current_density = 0.0
    
    def detect_emergency_vehicle(self) -> bool:
        # In a real implementation, this would interface with actual sensors
        return self.emergency_vehicle_present
    
    def get_traffic_density(self) -> float:
        # Returns traffic density between 0 and 1
        return self.current_density

# Class to represent a single traffic signal
class TrafficSignal:
    def __init__(self, signal_id: str, initial_state: SignalState = SignalState.RED):
        self.signal_id = signal_id
        self.current_state = initial_state
        self.default_durations = {
            SignalState.RED: 30,
            SignalState.YELLOW: 5,
            SignalState.GREEN: 25
        }
        self.current_duration = self.default_durations[initial_state]
    
    def change_state(self, new_state: SignalState) -> None:
        self.current_state = new_state
        self.current_duration = self.default_durations[new_state]
    
    def adjust_duration(self, new_duration: int) -> None:
        self.current_duration = new_duration

# Class to represent an intersection with multiple signals
class Intersection:
    def __init__(self, name: str):
        self.name = name
        self.signals: Dict[str, TrafficSignal] = {}
        self.traffic_detector = SensorBasedTrafficDetector()
        self.emergency_mode = False
    
    def add_signal(self, signal_id: str) -> None:
        self.signals[signal_id] = TrafficSignal(signal_id)
    
    def handle_emergency_vehicle(self) -> None:
        # Set all signals to red except the one in the emergency vehicle's direction
        self.emergency_mode = True
        for signal in self.signals.values():
            signal.change_state(SignalState.RED)
    
    def resume_normal_operation(self) -> None:
        self.emergency_mode = False

# Main controller class for the traffic signal system
class TrafficSignalController:
    def __init__(self):
        self.intersections: Dict[str, Intersection] = {}
        self.current_cycle = 0
    
    def add_intersection(self, intersection: Intersection) -> None:
        self.intersections[intersection.name] = intersection
    
    def update_signal_timings(self, traffic_density: float) -> None:
        # Adjust signal timings based on traffic density
        base_green_time = 25
        max_green_time = 45
        
        adjusted_time = base_green_time + int((max_green_time - base_green_time) * traffic_density)
        return adjusted_time
    
    def run_signal_cycle(self) -> None:
        for intersection in self.intersections.values():
            # Check for emergency vehicles
            if intersection.traffic_detector.detect_emergency_vehicle():
                intersection.handle_emergency_vehicle()
                continue
            
            # Normal operation
            traffic_density = intersection.traffic_detector.get_traffic_density()
            adjusted_green_time = self.update_signal_timings(traffic_density)
            
            # Update signal states
            for signal in intersection.signals.values():
                if signal.current_state == SignalState.GREEN:
                    signal.adjust_duration(adjusted_green_time)

# Example usage and demonstration
def main():
    # Create a controller
    controller = TrafficSignalController()
    
    # Create an intersection
    main_intersection = Intersection("Main and First")
    
    # Add signals to the intersection
    main_intersection.add_signal("NORTH")
    main_intersection.add_signal("SOUTH")
    main_intersection.add_signal("EAST")
    main_intersection.add_signal("WEST")
    
    # Add intersection to controller
    controller.add_intersection(main_intersection)
    
    # Simulate traffic signal operation
    while True:
        try:
            controller.run_signal_cycle()
            time.sleep(1)  # Update every second
        except KeyboardInterrupt:
            print("Traffic signal system shutting down...")
            break

if __name__ == "__main__":
    main()