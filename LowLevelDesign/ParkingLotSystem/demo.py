if __name__ == "__main__":
    # Create a parking lot with 3 levels
    parking_lot = ParkingLot(3)

    # Entry Gates
    entry_gate1 = EntryGate(1, parking_lot)
    entry_gate2 = EntryGate(2, parking_lot)

    # Exit Gate
    exit_gate = ExitGate(1, parking_lot)

    # Vehicles Arriving
    car = Car("CAR-123")
    motorcycle = Motorcycle("BIKE-456")
    truck = Truck("TRUCK-789")

    # Generate Tickets
    car_ticket = entry_gate1.generate_ticket(car)
    motorcycle_ticket = entry_gate2.generate_ticket(motorcycle)
    truck_ticket = entry_gate1.generate_ticket(truck)

    # Print Ticket Info
    if car_ticket:
        print("Car Ticket:", car_ticket.get_ticket_info())
    if motorcycle_ticket:
        print("Motorcycle Ticket:", motorcycle_ticket.get_ticket_info())
    if truck_ticket:
        print("Truck Ticket:", truck_ticket.get_ticket_info())

    # Exit Parking
    if exit_gate.process_exit(car_ticket):
        print("Car exited successfully")
    if exit_gate.process_exit(motorcycle_ticket):
        print("Motorcycle exited successfully")
    if exit_gate.process_exit(truck_ticket):
        print("Truck exited successfully")
