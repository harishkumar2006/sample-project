import datetime

class Vehicle:
    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.entry_time = None

class Slot:
    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.is_occupied = False
        self.vehicle = None

class ParkingLot:
    def __init__(self, total_slots):
        self.slots = [Slot(i) for i in range(1, total_slots + 1)]
        self.vehicles = {}

    def find_empty_slot(self):
        for slot in self.slots:
            if not slot.is_occupied:
                return slot
        return None

    def add_vehicle(self, vehicle):
        empty_slot = self.find_empty_slot()
        if empty_slot:
            empty_slot.is_occupied = True
            empty_slot.vehicle = vehicle
            vehicle.entry_time = datetime.datetime.now()
            self.vehicles[vehicle.vehicle_number] = empty_slot
            print(f"Vehicle {vehicle.vehicle_number} parked at slot {empty_slot.slot_number}")
        else:
            print("Parking is full!")

    def remove_vehicle(self, vehicle_number):
        if vehicle_number in self.vehicles:
            slot = self.vehicles[vehicle_number]
            slot.is_occupied = False
            parked_time = datetime.datetime.now() - slot.vehicle.entry_time
            fee = self.calculate_fee(parked_time)
            print(f"Vehicle {vehicle_number} removed from slot {slot.slot_number}")
            print(f"Parking fee: ${fee:.2f}")
            slot.vehicle = None
            del self.vehicles[vehicle_number]
        else:
            print("Vehicle not found!")

    def calculate_fee(self, parked_time):
        hours_parked = parked_time.total_seconds() / 3600
        return round(hours_parked) * 1  
parking_lot = ParkingLot(10) \vehicle1 = Vehicle("ABC123", "Car")
vehicle2 = Vehicle("XYZ789", "Bike")

parking_lot.add_vehicle(vehicle1)
parking_lot.add_vehicle(vehicle2)


import time
time.sleep(5) 
parking_lot.remove_vehicle("ABC123")
parking_lot.remove_vehicle("XYZ789")
