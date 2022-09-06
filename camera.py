import cv2
import time
from terminalTrueColors import *
from sys import stdout, argv
import argparse


def main(asciiChars, scale, color):
    cap = cv2.VideoCapture(0)
    cap.set(5, 60)

    #print(cap.get(5)) # fps
    width = int(cap.get(3))
    height = int(cap.get(4))
    #print("width: ", width)
    #print("height: ", height)

    

    while True:
        __, frame = cap.read()  
        scale_percent = scale # percent of original size
        imgWidth = int(width * scale_percent / 100)
        imgHeight = int(height * scale_percent / 100)
        dim = (imgWidth, imgHeight)
        newFrame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        output = ""
        for row in newFrame:
            for pixel in row:
                b = int(pixel[0])
                g = int(pixel[1])
                r = int(pixel[2])
                y = 0.299 * r +  0.587 * g + 0.114 * b
                if color:
                    output += cadd(rgb(r,g,b), asciiChars[int((y*len(asciiChars))//500)]*2)
                else:
                    output += asciiChars[int((y*len(asciiChars))//500)]*2
                
            output += "\n"
        print(output)
        stdout.flush()

        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Camera feed in terminal with ascii")
    parser.add_argument("--string", "-S", type=str, nargs="?", default="standard", help="string used (oldTV, standard, standardSmall and pixelated)")
    parser.add_argument("--customString", "-cs", type=str, nargs="?", default="NA", help="string used")
    parser.add_argument("--scale", "-s", type=int, nargs="?", default=30, help="scale of the camera feed")
    parser.add_argument("--color", "-c", type=bool, nargs="?", default=False, help="do you want color?")
    
    ns = parser.parse_args(argv[1:])

    asciiChars={
        "standard": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{[]?-_+~<>i!lI;:,^`'.      "[::-1],
        "standardSmall": " .:-=+*#%@",
        "oldTV": "▁▂▃▄▅▆▇▉█",
        "pixelated": "█"
    }

    if ns.customString == "NA":
        asciiChar = asciiChars[ns.string]
    else:
        asciiChar = ns.customString

    main(asciiChar,ns.scale,ns.color)