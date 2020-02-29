import tifffile
from scipy.ndimage import filters
import numpy as np
from datetime import datetime

from surfcut.cli import surfcut_parser
from surfcut.viewer.viewer import view


def main():
    args = surfcut_parser().parse_args()

    image_path = args.image_path

    print("Loading data")
    data = tifffile.imread(image_path)

    print("Smoothing image")
    filtered = np.copy(data)

    for idx, plane in enumerate(filtered):
        filtered[idx] = filters.gaussian_filter(plane, 3)


    view(data, filtered)


if __name__ == "__main__":
    main()
