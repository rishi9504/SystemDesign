import time
from enum import Enum
from threading import Thread
import redis

# Initialize Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Enum for Signal States
class SignalState(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"

# Traffic Signal Class
class TrafficSignal:
    def __init__(self, intersection_id, red_duration=30, yellow_duration=5, green_duration=30):
        self.intersection_id = intersection_id
        self.durations = {
            SignalState.RED: red_duration,
            SignalState.YELLOW: yellow_duration,
            SignalState.GREEN: green_duration,
        }
        self.current_state = SignalState.RED
        self.running = False

    def change_state(self, new_state):
        """Change the traffic signal state and persist to Redis."""
        self.current_state = new_state
        r.set(f"signal:{self.intersection_id}:state", self.current_state.value)
        print(f"Intersection {self.intersection_id}: Changed to {self.current_state.value}")

    def start(self):
        """Start the traffic signal cycle."""
        self.running = True
        while self.running:
            for state in [SignalState.GREEN, SignalState.YELLOW, SignalState.RED]:
                self.change_state(state)
                time.sleep(self.durations[state])

    def stop(self):
        """Stop the traffic signal."""
        self.running = False

# Emergency Override
class EmergencyHandler:
    def __init__(self, intersection_id):
        self.intersection_id = intersection_id

    def activate_emergency(self):
        """Set traffic signal to emergency state (flashing yellow)."""
        r.set(f"signal:{self.intersection_id}:state", SignalState.YELLOW.value)
        print(f"Intersection {self.intersection_id}: Emergency Mode Activated (Flashing Yellow)")

# Start the Traffic Signal System
if __name__ == "__main__":
    intersection_1 = TrafficSignal(intersection_id=1)
    signal_thread = Thread(target=intersection_1.start)
    signal_thread.start()
    
    time.sleep(10)  # Simulate normal operation
    emergency = EmergencyHandler(intersection_id=1)
    emergency.activate_emergency()
