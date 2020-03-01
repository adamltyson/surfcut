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

    down_shift = edges[0:-args.shift]
    padding = np.zeros((args.shift, edges.shape[1], edges.shape[2]))
    edges= np.append(padding, down_shift, axis=0)

    print("Shifting binary object down")
    shift_mag = int(args.depth / 2)
    down_shift = edges[0:-shift_mag]
    padding = np.zeros((shift_mag, edges.shape[1], edges.shape[2]))
    down_shift = np.append(padding, down_shift, axis=0)


    print("Shifting binary object up")
    up_shift = edges[shift_mag:]
    padding = np.zeros((shift_mag, edges.shape[1], edges.shape[2]))
    up_shift = np.append(up_shift, padding, axis=0)

    print("Generating mask")
    mask = up_shift - down_shift
    mask = mask > 0

    print("Masking data")
    masked = data * mask

    print("Projecting data")
    projection = np.max(masked, axis=0)

    print(f"Finished. Total time taken: {format(datetime.now() - start_time)}")

    print("Opening viewer")
    view(data, filtered, binary, edges, mask, masked, projection)


def edge_detect(image):
    edges = np.zeros_like(image)
    for idx, _ in enumerate(image):
        if idx < len(image):
            edges[idx, :, :] = np.max(image[0:idx+1], axis=0)

    return edges

if __name__ == "__main__":
    main()
