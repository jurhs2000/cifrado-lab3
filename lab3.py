# Universidad del Valle de Guatemala
# Cifrado de informacion
# Lab 3
# Julio Herrera
# Bryann Alfaro
# Diego Arredondo

import cifrados
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import PIL

result = cifrados.lgc(5, 3, 3, 7)
print(result)

img = PIL.Image.open("camera.png")

print(len(cifrados.read_image(img)))

newImg = cifrados.write_image(img, result)

showImg = mpimg.imread(newImg)
imgplot = plt.imshow(showImg)
plt.show()