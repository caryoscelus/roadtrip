init python:
    renpy.set_autoreload(False)

label start:
    play music main
    $ car = Car()
    $ location = StartingPoint()
    $ road = Road()
    # python:
        # for i in range(1, 100):
            # road.locations.append(GasStation(i*10.0))
    jump party.main
label party:
    $ road.position = location.position
    "You stop [location.description]"
label .main:
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
                tplus += 10.0 + random.random() * 20
                self.locations.append(random_location(self.position + tplus))
        def next_location(self):
            self.cleanup_locations()
            if not self.locations:
                self.generate_locations()
            return self.locations[0]
        def advance(self, d):
            self.position += d

    def random_hiker():
        # TODO
        return TestPerson("Rando")

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
        def add_pers(self, pers):
            if pers not in self.people:
                self.people.append(pers)
            return self.people.index(pers)
        def remove_pers(self, pers):
            if pers in self.people:
                self.people.remove(pers)

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
        def __init__(self, name, display):
            self.name = name
            self.display = display

    class Self(Person):
        def __init__(self):
            super().__init__('Myself', 'anonymous.png')

    class TestPerson(Person):
        def __init__(self, name):
            super().__init__(name, 'pers-1.png')

    class Car:
        def __init__(self):
            self.seat0 = None
            self.seat1 = None
            self.seat2 = None
            self.seat3 = None
        def remove_pers(self, pers):
            if self.seat1 is pers:
                self.seat1 = None
            if self.seat2 is pers:
                self.seat2 = None
            if self.seat3 is pers:
                self.seat3 = None
