class ParkingLot:
    def __init__(self, levels):
        """
        Constructor for ParkingLot class.

        The constructor takes one parameter, the number of levels in the parking lot.

        The constructor creates a list of ParkingLevel objects, each with a unique level
        id and 10 parking spots. The list is stored in the levels attribute of the
        ParkingLot object.

        The constructor also creates a threading.Lock() object and stores it in the
        lock attribute of the ParkingLot object. This lock is used to ensure thread
        safety when accessing the levels attribute of the ParkingLot object.

        :param levels: The number of levels in the parking lot
        :type levels: int
        """
        self.levels = [ParkingLevel(i, 10) for i in range(levels)]
        """
        A list of ParkingLevel objects, each representing a level in the parking lot
        """
        self.lock = Lock()
        """
        A threading.Lock() object, used to ensure thread safety when accessing the
        levels attribute of the ParkingLot object
        """

    def find_parking_spot(self, vehicle):
        """
        Find a parking spot for the given vehicle in the parking lot.

        This method takes one parameter, the vehicle to be parked.

        The method first acquires the lock on the levels attribute of the
        ParkingLot object. This ensures that no other thread can access the
        levels attribute at the same time.

        The method then iterates over the levels attribute of the ParkingLot
        object. For each ParkingLevel object in the levels attribute, the
        method calls the park_vehicle method of the ParkingLevel object and
        passes the vehicle as an argument.

        The park_vehicle method of the ParkingLevel object will return the
        spot_id of the parking spot where the vehicle was parked, or None if
        the vehicle cannot be parked.

        If the park_vehicle method returns a spot_id, the method returns a
        tuple of the level_id of the ParkingLevel object and the spot_id.

        If the park_vehicle method returns None for all ParkingLevel objects
        in the levels attribute, the method returns a tuple of None, None.

        :param vehicle: The vehicle to be parked
        :type vehicle: Vehicle
        :return: A tuple of the level_id and spot_id of the parking spot where
                 the vehicle was parked, or None, None if the vehicle cannot be
                 parked.
        :rtype: tuple
        """
        with self.lock:
            for level in self.levels:
                spot_id = level.park_vehicle(vehicle)
                if spot_id is not None:
                    return level.level_id, spot_id
        return None, None

    def release_parking_spot(self, level_id, spot_id):
        """
        Release a parking spot in the parking lot.

        This method takes two parameters, the level_id and the spot_id of the parking
        spot to be released.

        The method first acquires the lock on the levels attribute of the ParkingLot
        object. This ensures that no other thread can access the levels attribute
        while this thread is releasing a parking spot.

        Then, the method calls the release_spot() method of the ParkingLevel object
        that corresponds to the given level_id, passing the given spot_id as an
        argument.

        The method returns the result of the call to release_spot(), which is a
        boolean indicating whether the parking spot was successfully released.

        :param level_id: The level id of the parking spot to be released
        :type level_id: int
        :param spot_id: The spot id of the parking spot to be released
        :type spot_id: int
        :return: Whether the parking spot was successfully released
        :rtype: bool
        """
        with self.lock:
            return self.levels[level_id].release_spot(spot_id)
