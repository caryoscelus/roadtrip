screen hud:
    layer 'hud'
    fixed:
        text "[road.position:0.1f] km"
        text "cash [pc.money:0.1f]":
            ypos 40
        text "fuel":
            ypos 80
        bar value car.fuel range car.max_fuel:
            ypos 80
            xsize 200
