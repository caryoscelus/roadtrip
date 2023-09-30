init python:
    def person_dragged(pers):
        def dragged(drags, drop):
            drag = drags[0]
            print(drop)
            if drop is None:
                old_pos = drag.old_position
                drag.snap(old_pos[0], old_pos[1])
            else:
                drag.snap(drop.x, drop.y)
        return dragged

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
            use seat(1, 440, 380)
            use seat(2, 280, 520)
            use seat(3, 440, 520)

screen person(x, y, pers, is_draggable=True):
    if pers:
        drag:
            xpos x
            ypos y
            add Transform(pers.display, xzoom=0.5, yzoom=0.5)
            draggable is_draggable
            droppable False
            dragged person_dragged(pers)

screen seat(n, x, y):
    $ seat_name = f'seat_{n}'
    drag:
        drag_name seat_name
        xpos x
        ypos y
        add "empty.png"
        draggable False
        droppable True
