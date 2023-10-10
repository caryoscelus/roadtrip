"""renpy
init python:
"""

class Location:
    def __init__(self, position, display, description, people, scale=1, display_manage=""):
        self.position = position
        self.display = display
        self.display_manage = display_manage
        self.scale = scale
        self.description = description
        self.people = people
        self.luggage = [luggage for pers in people for luggage in pers.luggage]
        self.drop_spots = []
    def add_pers(self, pers):
        if pers not in self.people:
            self.people.append(pers)
        return self.people.index(pers)
    def add_luggage(self, luggage):
        if luggage not in self.luggage:
            self.luggage.append(luggage)
        return self.luggage.index(luggage)
    def add_item(self, item):
        if isinstance(item, Person):
            return self.add_pers(item)
        elif isinstance(item, Luggage):
            return self.add_luggage(item)
        else:
            raise ValueError("Can only add people or luggage to a location")
    def remove_pers(self, pers):
        if pers in self.people:
            self.people.remove(pers)
    def remove_luggage(self, luggage):
        if luggage in self.luggage:
            self.luggage.remove(luggage)
    def remove_item(self, item):
        if isinstance(item, Person):
            self.remove_pers(item)
        elif isinstance(item, Luggage):
            self.remove_luggage(item)
        else:
            raise ValueError("Can only remove people or luggage from a location")

class StartingPoint(Location):
    def __init__(self):
        super().__init__(0.0, None, "starting point", [pc], display_manage="tutorial.png")

class HikerPoint(Location):
    def __init__(self, position, people):
        super().__init__(position, 'hiker', "somewhere on the road", people)

class Spot:
    def __init__(self, x, y, f):
        self.x = x
        self.y = y
        if not f.startswith('spot_'):
            raise ValueError("Spot callback name should start with 'spot_'")
        self.f = f

GAS_PRICE = 10

def spot_pay_for_fuel(pers):
    if not isinstance(pers, Person):
        renpy.notify("Only people can pay for gas!")
        return
    if car.fuel >= car.max_fuel:
        renpy.notify("Tank is already full!")
        return
    if pers.money <= 0:
        renpy.notify(f"{pers.name} doesn't have money to pay for gas!")
        return
    bought_fuel = min(car.max_fuel-car.fuel, pers.money/GAS_PRICE)
    spent_money = bought_fuel*GAS_PRICE
    car.fuel += bought_fuel
    pers.money -= spent_money
    renpy.notify(f"Filled {bought_fuel:0.1f}l!")

class GasStation(Location):
    def __init__(self, position):
        super().__init__(position, 'gas-station', "at gas station", [], scale=1, display_manage="gas-station-manage.png")
        self.drop_spots = [Spot(730+140*2, 150, 'spot_pay_for_fuel')]
