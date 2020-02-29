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

    return parser