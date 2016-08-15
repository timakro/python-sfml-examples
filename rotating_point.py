#!/usr/bin/env python3
import sfml

window = sfml.RenderWindow(
    sfml.VideoMode(600,400),
    title="Rotating point",
    style=sfml.Style.CLOSE
)

RADIUS = 10
ROTATION_RADIUS = 100
ROTATION_SPEED = 0.05

circle = sfml.CircleShape()
circle.radius = RADIUS
circle.position = window.size/2
circle.fill_color = sfml.Color.RED
circle.origin = (circle.radius/2, ROTATION_RADIUS)

while window.is_open:
    for event in window.events:
        if type(event) == sfml.CloseEvent:
            window.close()

    circle.rotate(ROTATION_SPEED)
    window.clear()
    window.draw(circle)
    window.display()
