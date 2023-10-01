label road:
    $ update_sound(1.0, 10)
label .loop:
    $ road.advance(0.1)
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
    pause 0.1
    hide screen hiker
    return

label make_a_stop:
    $ i = 8
label .loop:
    call road_main
    $ road.advance(0.1*i/8)
    $ i -= 1
    if i > 0:
        jump .loop
    jump party

init python:
    def rideby(a, b, t):
        x = (128 ** t - 1) / 127
        return a * (1-x) + b * x

screen spot(dist, display, scale=1):
    fixed:
        imagebutton:
            idle display
            action Jump("make_a_stop")
            at transform:
                xpos int(rideby(1080, 1260, 1.0-dist/4))
                ypos int(rideby(420, -1200, 1.0-dist/4))
                zoom scale*rideby(0.04, 4.0, 1.0-dist/4)
