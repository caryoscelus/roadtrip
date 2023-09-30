label start:
    "One day I sold my apartment, bought a car and went on adventure."
    # create map
    # init location
    $ location = Location()
label main_loop:
    "You arrive at [location.description]"
    "Change party & items"
    "You are on the road!"
    jump main_loop
    # the game never ends, hehe
label exit:
    return

init python:
    class Location:
        def __init__(self):
            self.description = "Random location"
