label start:
    "One day I sold my apartment, bought a car and went on adventure."
    # create map
    # init location
    $ car = Car()
    $ location = Location()
label main_loop:
    "You arrive at [location.description]"
    "Change party & items"
    call screen location(location, car)
    "You are on the road!"
    call screen road(car)
    jump main_loop
    # the game never ends, hehe
label exit:
    return

init python:
    class Location:
        def __init__(self):
            self.description = "Random location"
            self.people = [TestPerson('Joanna'), Person('Joshua', 'pers-2.png'), TestPerson('Maria')]
        def add_pers(self, pers):
            if pers not in self.people:
                self.people.append(pers)
            return self.people.index(pers)
        def remove_pers(self, pers):
            if pers in self.people:
                self.people.remove(pers)

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
            self.seat0 = Self()
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
