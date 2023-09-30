label start:
    play music main
    $ car = Car()
    $ location = StartingPoint()
    $ road = Road()
label party:
    $ road.position = location.position
    hide screen hiker
    "You arrive at [location.description]"
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

    def random_location(position):
        return Location(position, "somewhere on the road", [TestPerson("Rando")])

    class Location:
        def __init__(self, position, description, people):
            self.position = position
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
            super().__init__(0.0, "starting point", [Self()])

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
