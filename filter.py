# importing required modules including functions from filters file
import sys
from cv2 import imread, imwrite, cvtColor, COLOR_BGR2RGB, COLOR_RGB2BGR
from filters import *
from os import path


# printing out the usage of program
def usage() -> None:
    print("Usage: filter [flag] infile outfile\nflags:\n-gray: grayscale\n-sep: sepia\n-refh: reflect horizontally\n-refv: reflect vertically\n-blur1: blur softly\n-blur2: blur normally\n-blur3: blur hardly")
    sys.exit(1)


# checking for proper usage
if len(sys.argv) != 4:
    usage()
elif (sys.argv[1] not in ["-gray", "-sep", "-refh", "-refv", "-blur1", "-blur2", "-blur3"]) or (not path.isfile(sys.argv[2])):
    usage()


# opening the image file and changing it to RGB mode
image = cvtColor(imread(sys.argv[2]), COLOR_BGR2RGB)

# applying the filter based on the flag
match sys.argv[1]:
	# grayscale
    case "-gray":
        grayscale(image)
	# sepia
    case "-sep":
        sepia(image)
	# horizontal reflect
    case "-refh":
        reflect_horizontally(image)
	# vertical reflect
    case "-refv":
        reflect_vertically(image)
	# blur 1 (soft)
    case "-blur1":
        blur1(image)
	# blur 2 (average)
    case "-blur2":
        blur2(image)
	# blur 3 (hard)
    case "-blur3":
        blur3(image)

# writing to argv[3] the BGR image
imwrite(sys.argv[3], cvtColor(image, COLOR_RGB2BGR))
