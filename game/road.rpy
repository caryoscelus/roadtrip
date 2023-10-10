init python:
    import math

    DAY_LENGTH = 600

label road:
    $ quick_menu = False
    $ update_sound(1.0, 10)
    $ already_stopping = False
label .loop:
    $ dist = car.drive(0.1)
    if dist == 0:
        jump stop_now
    call road_main
    jump .loop

label road_main:
    $ position = road.position
    $ shuffle_tracks(position)
    $ road_frame = str(int(road.position * 10) % 4)
    $ location = road.next_location()
    $ dist = location.position - position
    window hide
    scene expression "road-frame-000[road_frame].png"
    if 0 < dist <= 4:
        show screen spot(dist, location.display, location.scale)
    $ timeofday = time_now.t % DAY_LENGTH / DAY_LENGTH * 2 * math.pi
    $ darkness = math.sin(timeofday) * 0.8
    show night-filter onlayer effects:
        alpha darkness
    if darkness > 0.5:
        show lights onlayer effects:
            alpha 0.8
    else:
        hide lights
    pause 0.1
    hide screen hiker
    return

label make_a_stop:
    $ already_stopping = True
    $ i = 8
label .loop:
    call road_main
    $ dist = car.drive(0.1*i/8)
    if dist == 0:
        jump stop_now
    $ i -= 1
    if i > 0:
        jump .loop
    jump party

label stop_now:
    $ location = Location(road.position, '', "somewhere on the road", [])
    jump party

init python:
    def rideby(a, b, t):
        x = (128 ** t - 1) / 127
        return a * (1-x) + b * x

screen spot(dist, display, scale=1):
    layer 'master'
    fixed:
        imagebutton:
            if display == "hiker.png":
                focus_mask "hiker-click.png"
            idle display
            if not already_stopping:
                action Jump("make_a_stop")
            at transform:
                xpos int(rideby(1080, 1260, 1.0-dist/4))
                ypos int(rideby(420, -1200, 1.0-dist/4))
                zoom scale*rideby(0.04, 4.0, 1.0-dist/4)
