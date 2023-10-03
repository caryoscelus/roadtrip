"""renpy
init python:
"""

class Car:
    def __init__(self):
        self.seat0 = None
        self.seat1 = None
        self.seat2 = None
        self.seat3 = None
        self.trunk0 = None
        self.trunk1 = None
        self.fuel = 60
    def burn_fuel(self, t):
        return t
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
