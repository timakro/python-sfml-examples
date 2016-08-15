#!/usr/bin/env python3
import sfml
import math

window = sfml.RenderWindow(
    sfml.VideoMode(640, 480),
    title="Use P and M key to change window size",
    style=sfml.Style.CLOSE
)

def resize_window(diff):
    window.recreate(
        sfml.VideoMode(window.size.x + diff, window.size.y + diff),
        title="Use P and M key to change window size",
        style=sfml.Style.CLOSE
    )

clock = sfml.Clock()

circle = sfml.CircleShape()
circle.fill_color = sfml.Color(255, 200, 200)
circle.outline_color = sfml.Color(255, 100, 100)
circle.outline_thickness = 5

while window.is_open:
    for event in window.events:
        if type(event) == sfml.KeyEvent and event.pressed:
            if event.code == sfml.Keyboard.P:
                resize_window(+10)
            if event.code == sfml.Keyboard.M:
                resize_window(-10)
        elif type(event) == sfml.CloseEvent:
            window.close()

    circle.radius = 50 + 10*math.sin(clock.elapsed_time.seconds)
    circle.position = window.size/2 - circle.global_bounds.size/2

    window.clear(sfml.Color.RED)
    window.draw(circle)
    window.display()
