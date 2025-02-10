# Parking Spot Class
class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        """
        Constructor for ParkingSpot class.

        The constructor takes two parameters: the unique id of the parking spot
        and the type of vehicle that can be parked in the spot.

        The constructor sets the spot_id and spot_type attributes of the
        ParkingSpot object to the values of the parameters. It also sets the
        status attribute to SpotStatus.AVAILABLE, indicating that the spot is
        available for parking. Finally, it sets the vehicle attribute to None,
        indicating that there is no vehicle currently parked in the spot.

        :param spot_id: Unique id of the parking spot
        :type spot_id: int
        :param spot_type: Type of vehicle that can be parked in the spot
        :type spot_type: VehicleType
        """
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
