import sys
from cv2 import imread, imwrite, cvtColor, COLOR_BGR2RGB, COLOR_RGB2BGR
from filters import *
from os import path


def usage():
    print(
        "Usage: filter [flag] infile outfile\nflags:\n-gray: grayscale\n-sep: sepia\n-refh: reflect horizontally\n-refv: reflect vertically\n-blur1: blur softly\n-blur2: blur normally\n-blur3: blur hardly"
    )
    sys.exit(1)


if len(sys.argv) != 4:
    usage()
elif (sys.argv[1] not in ["-gray", "-sep", "-refh", "-refv", "-blur1", "-blur2", "-blur3"]) or (not path.isfile(sys.argv[2])):
    usage()


image = cvtColor(imread(sys.argv[2]), COLOR_BGR2RGB)
match sys.argv[1]:
    case "-gray":
        grayscale(image)
    case "-sep":
        sepia(image)
    case "-refh":
        reflect_horizontally(image)
    case "-refv":
        reflect_vertically(image)
    case "-blur1":
        blur1(image)
    case "-blur2":
        blur2(image)
    case "-blur3":
        blur3(image)

imwrite(sys.argv[3], cvtColor(image, COLOR_RGB2BGR))
