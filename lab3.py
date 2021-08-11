# Universidad del Valle de Guatemala
# Cifrado de informacion
# Lab 3
# Julio Herrera
# Bryann Alfaro
# Diego Arredondo

import cifrados
import matplotlib.pyplot as plt
from PIL import Image

resultLGC = cifrados.lgc(5, 3, 3, 7)
print(f"LGC: {resultLGC}")

resultWichman = cifrados.wichman(134,1455,1132)
print(f"Wichman: {resultWichman}")

# load image as pixel array

img = Image.open('camera.png').convert('L') # L = 8-bit pixels, black and white
img.show()

a = cifrados.read_image(img)

I = cifrados.write_image(a, img)
plt.figure()
plt.imshow(I,cmap='gray')
plt.show()
