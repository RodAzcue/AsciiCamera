
from PIL import Image
from terminalTrueColors import *

#im = Image.open('image.jpg', 'r')
#im = Image.open('test.webp', 'r')
#im = Image.open('perfil.jpg', 'r')
im = Image.open('matrix.png', 'r')
new_image = im.resize((1000, 1000))
pix_val = list(new_image.getdata())


asciiGrayScale = '█@B%8&WM#*oah▓b▒p░≡=-O0QLCJUYX.cvunxrjft/|()1{[]?-_+~<>i!lI;:,"^`.'[::-1]
azcueGrayScale = "█▓▓▓▓▒▒▒▒░░░░####≡≡≡≡====----....                     "
thereisanother = "█▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░"
yetanother = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{[]?-_+~<>i!lI;:,^`'."


scale = yetanother
def nose(y):
	return int((y*len(scale))//500)

for i, pixel in enumerate(pix_val):
	r = pixel[0]
	g = pixel[1]
	b = pixel[2]
	y = 0.299 * r +  0.587 * g + 0.114 * b

	print(cadd(rgb(r,g,b), scale[nose(y)]*2),end='')
	if i % new_image.size[0] == 0:
		print()


types = ["─", "═","░", "▒", "▓", "█", "-",  "=",  "≡",  "≡", "¯", "#"]
