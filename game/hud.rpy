screen hud:
    layer 'hud'
    fixed:
        text "[road.position:0.0f] km"
        text "cash [pc.money:0.1f]":
            ypos 40
        bar value car.fuel range car.max_fuel:
            ypos 80
            xsize 200
        text "fuel":
            ypos 80
