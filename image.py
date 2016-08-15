#!/usr/bin/env python3
import sfml

window = sfml.RenderWindow(
    sfml.VideoMode(640, 480),
    title="Displaying an image",
    style=sfml.Style.CLOSE
)

texture = sfml.Texture.from_file('images/tree.png')
sprite = sfml.Sprite(texture)
sprite.position = window.size/2 - sprite.global_bounds.size/2

while window.is_open:
    for event in window.events:
        if type(event) == sfml.CloseEvent:
            window.close()

    window.clear(sfml.Color.WHITE)
    window.draw(sprite)
    window.display()
