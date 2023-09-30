label road:
    $ position = road.position
    $ road_frame = str(int(road.position * 10) % 4)
    $ location = road.next_location()
    $ dist = location.position - position
    window hide
    scene expression "road-frame-000[road_frame].png"
    if 0 < dist <= 4:
        show screen hiker(dist)
    pause 0.1
    hide screen hiker
    $ road.advance(0.1)
    jump road

init python:
    def rideby(a, b, t):
        x = (32 ** t - 1) / 31
        return a * (1-x) + b * x

screen hiker(dist):
    fixed:
        imagebutton:
            idle "hiker.png"
            action Jump("party")
            at transform:
                xpos int(rideby(1080, 2260, 1.0-dist/4))
                ypos int(rideby(390, 320, 1.0-dist/4))
                zoom rideby(0.04, 1.0, 1.0-dist/4)
