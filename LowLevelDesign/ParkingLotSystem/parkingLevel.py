class ParkingLevel:
    def __init__(self, level_id, num_spots):
        """
        Constructor for ParkingLevel class.

        :param level_id: Unique identifier for the parking level
        :type level_id: int
        :param num_spots: Total number of parking spots in the level
        :type num_spots: int
        """
        self.level_id = level_id  # Unique identifier for the parking level
        self.spots = []  # List of parking spots in the level
        self.lock = Lock()  # Ensuring thread safety for the list of parking spots

        # Creating different spots for different vehicle types
        for i in range(num_spots):
            # Every 3rd spot is a truck spot
            if i % 3 == 0:
                self.spots.append(ParkingSpot(
                    i,  # Unique identifier for the parking spot
                    VehicleType.TRUCK  # Vehicle type for the parking spot
                ))
            # Every 3rd spot after a truck spot is a car spot
            elif i % 3 == 1:
                self.spots.append(ParkingSpot(
                    i,  # Unique identifier for the parking spot
                    VehicleType.CAR  # Vehicle type for the parking spot
                ))
            # Every 3rd spot after a car spot is a motorcycle spot
            else:
                self.spots.append(ParkingSpot(
                    i,  # Unique identifier for the parking spot
                    VehicleType.MOTORCYCLE  # Vehicle type for the parking spot
                ))

    def find_available_spot(self, vehicle_type):
        # Acquire a lock to ensure thread safety when accessing parking spots
        with self.lock:
            # Iterate over each parking spot in the level
            for spot in self.spots:
                # Check if the spot is available and matches the required vehicle type
                if spot.status == SpotStatus.AVAILABLE and spot.spot_type == vehicle_type:
                    # Return the first available spot that matches the vehicle type
                    return spot
        # Return None if no suitable spot is found
        return None

    def park_vehicle(self, vehicle):
        # Attempt to find an available parking spot that matches the vehicle's type
        spot = self.find_available_spot(vehicle.vehicle_type)
        
        # Check if a suitable spot is found
        if spot:
            # Assign the vehicle to the found spot
            spot.assign_vehicle(vehicle)
            # Return the unique identifier of the parking spot
            return spot.spot_id
        
        # Return None if no suitable spot was found
        return None

    def release_spot(self, spot_id):
        """
        Release a parking spot in the parking level.

        This method takes one parameter, the unique identifier of the parking
        spot to be released.

        The method first acquires the lock on the parking level to ensure thread
        safety when modifying the parking spots.

        Then, the method iterates over each parking spot in the level and checks
        if the unique identifier of the parking spot matches the given spot_id.

        If a matching spot is found, the method calls the release_spot() method
        of the parking spot to release the vehicle in the spot.

        The method returns True if a matching spot was found and released, or
        False if no matching spot was found.
        """
        with self.lock:
            # Iterate over each parking spot in the level
            for spot in self.spots:
                # Check if the parking spot matches the given spot_id
                if spot.spot_id == spot_id:
                    # Release the vehicle in the parking spot
                    spot.release_spot()
                    # Return True to indicate success
                    return True
        # Return False to indicate failure
        return False
