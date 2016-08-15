#!/usr/bin/env python3
import sfml

window = sfml.RenderWindow(
    sfml.VideoMode(640, 480),
    title="Just a button",
    style=sfml.Style.CLOSE
)

DEFAULT_COLOR = sfml.Color(48, 165, 255)
PRESS_COLOR = sfml.Color(0, 144, 255)
MARGIN = 50

text = sfml.Text("Useless Button")
text.font = sfml.Font.from_file('fonts/DejaVuSerif.ttf')
text.character_size = 50
text.color = sfml.Color.BLACK
text.position = window.size/2 - text.global_bounds.size/2

rect = sfml.RectangleShape()
rect.size = text.global_bounds.size + 2*MARGIN
rect.fill_color = DEFAULT_COLOR
rect.position = window.size/2 - rect.size/2

while window.is_open:
    for event in window.events:
        if type(event) == sfml.MouseButtonEvent:
            if (event.button == sfml.Mouse.LEFT and
                rect.global_bounds.contains(event.position)):
                if event.pressed:
                    rect.fill_color = PRESS_COLOR
                elif event.released:
                    rect.fill_color = DEFAULT_COLOR
        elif type(event) == sfml.CloseEvent:
            window.close()


    window.clear(sfml.Color.WHITE)
    window.draw(rect)
    window.draw(text)
    window.display()
