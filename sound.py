#!/usr/bin/env python3
import sfml

window = sfml.RenderWindow(
    sfml.VideoMode(640, 480),
    title="Sound test",
    style=sfml.Style.CLOSE
)

DEFAULT_COLOR = sfml.Color(255, 165, 48)
PRESS_COLOR = sfml.Color(255, 144, 0)
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

sound_buffer = sfml.SoundBuffer.from_file('audio/fart.wav')
high_sound = sfml.Sound()
high_sound.buffer = sound_buffer
high_sound.pitch = 1.1
deep_sound = sfml.Sound()
deep_sound.buffer = sound_buffer

while window.is_open:
    for event in window.events:
        if type(event) == sfml.MouseButtonEvent:
            if (event.button == sfml.Mouse.LEFT and
                rect.global_bounds.contains(event.position)):
                if event.pressed:
                    rect.fill_color = PRESS_COLOR
                    high_sound.play()
                elif event.released:
                    rect.fill_color = DEFAULT_COLOR
                    deep_sound.play()
        elif type(event) == sfml.CloseEvent:
            window.close()

    window.clear(sfml.Color.WHITE)
    window.draw(rect)
    window.draw(text)
    window.display()
