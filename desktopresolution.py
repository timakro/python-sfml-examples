import sfml

desktop = sfml.VideoMode.get_desktop_mode()
resolution, bpp = desktop
width, height = resolution

window = sfml.RenderWindow(
    sfml.VideoMode(width, height, bpp),
    title="Get default system resolution",
    style=sfml.Style.FULLSCREEN
)

print("List of supported FullScreen resolutions")
i = 0
modes = sfml.VideoMode.get_fullscreen_modes()
for mode in modes:
        print("Mode #{0}: {1}".format(i, mode))
        i += 1


while window.is_open:
    for event in window.events:
        if type(event) == sfml.CloseEvent:
            window.close()

    window.clear(sfml.Color.RED)
    window.display()
