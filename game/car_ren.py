"""renpy
init python:
"""

# 3 tanks / 24h
FUEL_CONSUMPTION = 0.3
DISTANCE_PER_FUEL = 1 / FUEL_CONSUMPTION

class Car:
    def __init__(self):
        self.seat0 = None
        self.seat1 = None
        self.seat2 = None
        self.seat3 = None
        self.trunk0 = None
        self.trunk1 = None
        self.max_fuel = 60
        self.fuel = self.max_fuel
    def drive(self, t):
        need_fuel = t * FUEL_CONSUMPTION
        burned_fuel = min(need_fuel, self.fuel)
        self.fuel -= burned_fuel
        distance = DISTANCE_PER_FUEL * burned_fuel
        # TODO
        road.advance(distance)
        time_now.passed(t)
        return distance
    def remove_item(self, item):
        if self.seat0 is item:
            self.seat0 = None
        if self.seat1 is item:
            self.seat1 = None
        if self.seat2 is item:
            self.seat2 = None
        if self.seat3 is item:
            self.seat3 = None
        if self.trunk0 is item:
            self.trunk0 = None
        if self.trunk1 is item:
            self.trunk1 = None
    def people(self):
        return [item for item in (self.seat0, self.seat1, self.seat2, self.seat3) if isinstance(item, Person)]
    def luggage(self):
        return [item for item in
                (self.seat0, self.seat1, self.seat2, self.seat3, self.trunk0, self.trunk1)
                if isinstance(item, Luggage)]
