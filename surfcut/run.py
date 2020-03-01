import tifffile
from scipy.ndimage import filters
import numpy as np
from datetime import datetime

from surfcut.cli import surfcut_parser
from surfcut.viewer.viewer import view


# TODO: don't use unique image variable names, otherwise they all sit in ram.
# Doing this initially for visualisation

def main():
    start_time = datetime.now()
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
    binary = filtered > args.threshold

    print("Detecting edges")
    edges = edge_detect(binary)
    print(f"Finished. Total time taken: {format(datetime.now() - start_time)}")
    view(data, filtered, binary, edges)


def edge_detect(image):
    edges = np.zeros_like(image)
    for idx, _ in enumerate(image):
        if idx < len(image):
            edges[idx, :, :] = np.max(image[0:idx+1], axis=0)

    return edges

if __name__ == "__main__":
    main()
