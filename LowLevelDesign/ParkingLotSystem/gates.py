class EntryGate:
    def __init__(self, gate_id, parking_lot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot

    def generate_ticket(self, vehicle):
        """
        Generate a ticket for the given vehicle.

        :param vehicle: the vehicle to generate a ticket for
        :type vehicle: Vehicle
        :return: a ticket for the vehicle or None if the vehicle cannot be parked
        :rtype: Ticket or None
        """
        # Find a parking spot for the vehicle
        level_id, spot_id = self.parking_lot.find_parking_spot(vehicle)

        # If a parking spot is found, generate a ticket
        if spot_id is not None:
            return Ticket(vehicle, level_id, spot_id)
        else:
            # Otherwise return None to indicate failure
            return None

class ExitGate:
    def __init__(self, gate_id, parking_lot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot

    def process_exit(self, ticket):
        return self.parking_lot.release_parking_spot(ticket.level_id, ticket.spot_id)
