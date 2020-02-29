import napari

def view(*args):
    with napari.gui_qt():
        v = napari.Viewer(title="Surfcut")
        for image in args:
                v.add_image(image)
