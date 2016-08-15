#!/usr/bin/env python3
import sfml

window = sfml.RenderWindow(
    sfml.VideoMode(640, 480),
    title="My first pySFML window"
)

while window.is_open:
    for event in window.events:
        if type(event) == sfml.CloseEvent:
            window.close()

    window.clear(sfml.Color.RED)
    window.display()
