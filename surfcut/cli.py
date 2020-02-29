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
        type=float,
        default=3,
        help="Gaussian smoothing sigma width",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        dest="threshold",
        type=float,
        default=20,
        help="Threshold for binarising the image",
    )
    return parser