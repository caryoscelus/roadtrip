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
    jump main_loop
    # the game never ends, hehe
label exit:
    return

init python:
    class Location:
        def __init__(self):
            self.description = "Random location"
            self.people = [TestPerson(), TestPerson()]

    class Person:
        def __init__(self, display):
            self.display = display

    class Self(Person):
        def __init__(self):
            super().__init__('anonymous.png')

    class TestPerson(Person):
        def __init__(self):
            super().__init__('pers-1.png')

    class Car:
        def __init__(self):
            self.seat0 = Self()
            self.seat1 = None
            self.seat2 = None
            self.seat3 = None
