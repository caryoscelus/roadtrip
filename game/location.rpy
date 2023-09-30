screen location(location, car):
    fixed:
        add "manage.png"
        textbutton "Hit the road!" action Return():
            xalign 0.5
            ypos 0.9
        draggroup:
            use person(280, 380, car.seat0, False)
            use person(440, 380, car.seat1)
            use person(280, 520, car.seat2)
            use person(440, 520, car.seat3)
            for i, pers in enumerate(location.people):
                use person(730, 150+i*140, pers)

screen person(x, y, seat, is_draggable=True):
    if seat:
        drag:
            xpos x
            ypos y
            draggable is_draggable
            add Transform(seat.display, xzoom=0.5, yzoom=0.5)
