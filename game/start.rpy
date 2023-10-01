init python:
    def populate_gasstations():
        for i in range(1, 100):
            road.locations.append(GasStation(i*10.0))

label start:
    $ init_music()
    $ car = Car()
    $ location = StartingPoint()
    $ road = Road()
    jump party.main
label party:
    $ update_sound(0.0, 10)
    $ road.position = location.position
    "You stop [location.description]"
label .main:
    hide lights
    hide screen spot
    call screen location(location, car)
    jump road
    # the game never ends, hehe
label exit:
    return

init python:
    import random

    class Road:
        def __init__(self):
            self.position = 0.0
            self.locations = []
        def cleanup_locations(self):
            while self.locations and self.locations[0].position < self.position:
                self.locations.pop(0)
        def generate_locations(self):
            tplus = 0
            while tplus < 60.0:
                tplus += 6.0 + random.random() * 18.0
                self.locations.append(random_location(self.position + tplus))
        def next_location(self):
            self.cleanup_locations()
            if not self.locations:
                self.generate_locations()
            return self.locations[0]
        def advance(self, d):
            self.position += d

    def random_name():
        return short_names[int(random.random()*len(short_names))]

    def random_display():
        ndisplay = 4
        return f'pers-{int(random.random()*ndisplay):04}.png'

    def random_hiker():
        name = random_name()
        display = random_display()
        random_choice = random.random()*10
        if random_choice < 1:
            count = 2
        elif random_choice < 5:
            count = 1
        else:
            count = 0
        pers = Person(name, display, [])
        pers.luggage = [Luggage('luggage.png', pers) for _ in range(count)]
        return pers

    def random_hikers():
        random_choice = random.random()*10
        if random_choice < 1:
            count = 3
        elif random_choice < 3:
            count = 2
        else:
            count = 1
        return [random_hiker() for _ in range(count)]

    def random_location(position):
        random_choice = random.random()*10
        if random_choice < 3:
            return GasStation(position)
        else:
            return HikerPoint(position, random_hikers())

    class Location:
        def __init__(self, position, display, description, people, scale=1):
            self.position = position
            self.display = display
            self.scale = scale
            self.description = description
            self.people = people
            self.luggage = [luggage for pers in people for luggage in pers.luggage]
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
            super().__init__(0.0, None, "starting point", [Self()])

    class HikerPoint(Location):
        def __init__(self, position, people):
            super().__init__(position, 'hiker', "somewhere on the road", people)

    class GasStation(Location):
        def __init__(self, position):
            super().__init__(position, 'gas-station', "at gas station", [], scale=1)

    class Person:
        def __init__(self, name, display, luggage):
            self.name = name
            self.display = display
            self.luggage = luggage

    class Self(Person):
        def __init__(self):
            super().__init__('You', 'anonymous.png', [MyLuggage(self)])

    class TestPerson(Person):
        def __init__(self, name):
            super().__init__(name, 'pers-1.png', [])

    class Luggage:
        def __init__(self, display, owner):
            self.display = display
            self.owner = owner

    class MyLuggage(Luggage):
        def __init__(self, owner):
            super().__init__('luggage.png', owner)

    class Car:
        def __init__(self):
            self.seat0 = None
            self.seat1 = None
            self.seat2 = None
            self.seat3 = None
            self.trunk0 = None
            self.trunk1 = None
        def remove_item(self, item):
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
