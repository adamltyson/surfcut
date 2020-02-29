import tifffile

from surfcut.cli import surfcut_parser
from surfcut.viewer.viewer import view


def main():
    args = surfcut_parser().parse_args()

    image_path = args.image_path
    print(image_path)
    data = tifffile.imread(image_path)

    print(data.shape)
    view(data)




if __name__ == "__main__":
    main()
