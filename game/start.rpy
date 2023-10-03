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
        # 0 - 200 tg for paying
        money = int(random.random() * 20) * 10
        pers = Person(name, display, [], money)
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
        def __init__(self, position, display, description, people, scale=1, display_manage=""):
            self.position = position
            self.display = display
            self.display_manage = display_manage
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
            super().__init__(0.0, None, "starting point", [Self()], display_manage="tutorial.png")

    class HikerPoint(Location):
        def __init__(self, position, people):
            super().__init__(position, 'hiker', "somewhere on the road", people)

    class GasStation(Location):
        def __init__(self, position):
            super().__init__(position, 'gas-station', "at gas station", [], scale=1, display_manage="gas-station-manage.png")
