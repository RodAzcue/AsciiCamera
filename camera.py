import cv2
import time
from terminalTrueColors import *
from sys import stdout


cap = cv2.VideoCapture(0)
cap.set(5, 60)

framecount = 0
prevMillis = 0

print(cap.get(5)) # fps
width = int(cap.get(3))
height = int(cap.get(4))

print("width: ", width)
print("height: ", height)
"""
def fpsCount():
    global prevMillis
    global framecount
    millis = int(round(time.time() * 1000))
    framecount += 1
    if millis - prevMillis > 1000:
        print(framecount)
        prevMillis = millis 
        framecount = 0
"""
yetanother = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{[]?-_+~<>i!lI;:,^`'."
azcueGrayScale = "█▓▒░$%@#≡;:=_-,.'`                                              "
#azcueGrayScale = "█▓▒░░≡=-,
test= "▁▂▃▄▅▆▇▉█"


scale = "█"
def nose(y):
    return int((y*len(scale))//500)



while True:
    __, frame = cap.read()
    #print(len(frame))
    #print(len(frame[0]))
    #print(len(frame[0][0]))
    #print()
    
    scale_percent = 10 # percent of original size
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
            output += cadd(rgb(r,g,b), scale[nose(y)]*2)
            #output += scale[nose(y)]*2
            
        output += "\n"
    print(output)
    stdout.flush()

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #blur = cv2.blur(frame, (5, 5))
    #ret, thresh = cv2.threshold(blur, 170, 255, 0)
    #cv2.imshow("Image", frame)


    #fpsCount()   
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()