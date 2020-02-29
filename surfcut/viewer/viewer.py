import napari

def view(array):
    with napari.gui_qt():
        v = napari.Viewer(title="Surfcut")
        v.add_image(array)
