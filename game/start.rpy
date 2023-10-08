init python:
    def populate_gasstations():
        for i in range(1, 100):
            road.locations.append(GasStation(i*10.0))

label start:
    $ init_music()
    $ car = Car()
    $ location = StartingPoint()
    $ road = Road()
    $ time_now.init(0.0)
    show screen hud
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
