# Universidad del Valle de Guatemala
# Cifrado de informacion
# Lab 3
# Julio Herrera
# Bryann Alfaro
# Diego Arredondo

import cifrados
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

import PIL

result = cifrados.lgc(5, 3, 3, 7)
print(result)

img = PIL.Image.open("camera.png")
cifrados.wichman(134,1455,1132)
print(len(cifrados.read_image(img)))
print(cifrados.wichman(134,1455,1132))

newImg = cifrados.write_image(img, result)

showImg = mpimg.imread(newImg)
imgplot = plt.imshow(showImg)


plt.show()
cifrados.wichman(134,1455,1132)