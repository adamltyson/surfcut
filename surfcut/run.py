import tifffile
from scipy.ndimage import filters
import numpy as np
from datetime import datetime

from surfcut.cli import surfcut_parser
from surfcut.viewer.viewer import view


# TODO: don't use unique image variable names, otherwise they all sit in ram.
# Doing this initially for visualisation

def main():
    args = surfcut_parser().parse_args()

    image_path = args.image_path

    print("Loading data")
    data = tifffile.imread(image_path)

    print("Converting to 8 bit")
    data = data.astype(np.uint8)

    print("Smoothing")
    filtered = np.copy(data)
    for idx, plane in enumerate(filtered):
        filtered[idx] = filters.gaussian_filter(plane, args.gauss_sigma)

    print("Thresholding")
    binary = 1.0 * (filtered > args.threshold)

    print("Detecting edges")
    edges = edge_detect(binary)
    view(data, filtered, binary, edges)


def edge_detect(image):
    # // Edge
    # detect
    # getDimensions(w, h, channels, slices, frames);
    # print(slices);
    # for (img=0; img < slices; img++){
    #     print("Edge detect projection" + img + "/" + slices);
    # slice = img+1;
    # selectWindow(imgName);
    # run("Z Project...", "stop=&slice projection=[Max Intensity]");
    # }

    # FIXME: why doesnt this work?
    edges = np.zeros_like(image)
    for idx, _ in enumerate(image):
        if idx < len(image):
            edges[idx, :, :] = np.max(image[0:idx+1], axis=0)

    return edges

if __name__ == "__main__":
    main()
