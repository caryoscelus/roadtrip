init python:
    location_error_message = None

    def person_dragged(pers):
        def dragged(drags, drop):
            drag = drags[0]
            old_pos = drag.old_position
            if drop is None:
                drag.snap(old_pos[0], old_pos[1])
            elif drop.drag_name == 'street':
                car.remove_pers(pers)
                index = location.add_pers(pers)
                drag.snap(730, 150+index*140)
                renpy.restart_interaction()
            else:
                if getattr(car, drop.drag_name) is not None:
                    drag.snap(old_pos[0], old_pos[1])
                else:
                    drag.snap(drop.x, drop.y)
                    car.remove_pers(pers)
                    location.remove_pers(pers)
                    setattr(car, drop.drag_name, pers)
                    renpy.restart_interaction()
                    # unfortunately restart_interaction is glitching so we have to
                    # manually snap the person we didn't really dragged
                    fix_screen_locations()
        return dragged

    def fix_screen_locations():
        locscreen = renpy.get_screen('location')
        drag_group = locscreen.child.child.child
        for drag in drag_group.children:
            x, y = drag.old_position[:2]
            drag.snap(x, y)

    class TryToGo(Return):
        def __call__(self):
            if car.seat0 is None:
                renpy.notify("Car won't drive without a driver!")
                return None
            lacking_luggage = False
            for pers in car.people():
                for luggage in pers.luggage:
                    if luggage not in car.luggage():
                        renpy.notify(f"{pers.name} won't travel without their luggage!")
                        lacking_luggage = True
            if lacking_luggage:
                return None
            return super().__call__()

screen location(location, car):
    fixed:
        add "manage.png"
        textbutton "Hit the road!" action TryToGo():
            xalign 0.5
            ypos 0.9
        draggroup:
            use person(280, 380, car.seat0, False)
            use person(440, 380, car.seat1)
            use person(280, 520, car.seat2)
            use person(440, 520, car.seat3)
            # luggage
            use person(280, 760, car.trunk0)
            use person(440, 760, car.trunk1)
            for i, pers in enumerate(location.people):
                use person(730, 150+i*140, pers)
                for j, luggage in enumerate(pers.luggage):
                    if luggage not in car.luggage():
                        use person(730+(j+1)*140, 150+i*140, luggage)
            use seat(0, 280, 380)
            use seat(1, 440, 380)
            use seat(2, 280, 520)
            use seat(3, 440, 520)
            use trunk(0, 280, 760)
            use trunk(1, 440, 760)
            drag:
                drag_name 'street'
                xpos 730
                ypos 150
                add "empty-street.png"
                draggable False
                droppable True

screen person(x, y, pers, is_draggable=True):
    if pers:
        drag:
            # drag_name pers.name
            xpos x
            ypos y
            add Transform(pers.display, xzoom=0.5, yzoom=0.5)
            draggable is_draggable
            droppable False
            dragged person_dragged(pers)

screen seat(n, x, y):
    $ seat_name = f'seat{n}'
    drag:
        drag_name seat_name
        xpos x
        ypos y
        add "empty.png"
        draggable False
        droppable True

screen trunk(n, x, y):
    $ seat_name = f'trunk{n}'
    drag:
        drag_name seat_name
        xpos x
        ypos y
        add "empty.png"
        draggable False
        droppable True
