#!/usr/bin/env python3
import sfml

desktop = sfml.VideoMode.get_desktop_mode()
resolution, bpp = desktop
width, height = resolution

window = sfml.RenderWindow(
    sfml.VideoMode(width, height, bpp),
    title="Fullscreen, click to exit",
    style=sfml.Style.FULLSCREEN
)

rect1 = sfml.RectangleShape()
rect1.size = (100, 100)
rect1.fill_color = sfml.Color.BLACK
rect1.position = (0, 0)
rect2 = sfml.RectangleShape()
rect2.size = (100, 100)
rect2.fill_color = sfml.Color.BLACK
rect2.position = window.size - rect2.size

while window.is_open:
    for event in window.events:
        if (type(event) == sfml.CloseEvent or
            type(event) == sfml.MouseButtonEvent):
            window.close()

    window.clear(sfml.Color.RED)
    window.draw(rect1)
    window.draw(rect2)
    window.display()
