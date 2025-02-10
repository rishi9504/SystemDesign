import uuid
from datetime import datetime

class Ticket:
    def __init__(self, vehicle, level_id, spot_id):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.level_id = level_id
        self.spot_id = spot_id
        self.entry_time = datetime.now()

    def get_ticket_info(self):
        return {
            "ticket_id": self.ticket_id,
            "vehicle": self.vehicle.license_plate,
            "level_id": self.level_id,
            "spot_id": self.spot_id,
            "entry_time": self.entry_time.strftime("%Y-%m-%d %H:%M:%S")
        }
