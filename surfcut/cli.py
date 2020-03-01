from argparse import (
    ArgumentParser,
    ArgumentDefaultsHelpFormatter,
)

def surfcut_parser():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        dest="image_path",
        type=str,
        nargs=1,
        help="Path to the image to be analysed",
    )
    parser.add_argument(
        "-g",
        "--gauss_sigma",
        dest="gauss_sigma",
        type=int,
        default=3,
        help="Gaussian smoothing sigma width",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        dest="threshold",
        type=int,
        default=20,
        help="Threshold for binarising the image",
    )
    parser.add_argument(
        "-s",
        "--shift-magnitude",
        dest="shift_magnitude",
        type=int,
        default=15,
        help="Thickness of the surface projection",
    )
    return parser