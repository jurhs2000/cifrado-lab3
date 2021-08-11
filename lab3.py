# Universidad del Valle de Guatemala
# Cifrado de informacion
# Lab 3
# Julio Herrera
# Bryann Alfaro
# Diego Arredondo

import cifrados
import matplotlib.pyplot as plt
from PIL import Image

def show_image(I):
    plt.figure()
    plt.imshow(I,cmap='gray')
    plt.show()

# load image as pixel array

img = Image.open('camera.png').convert('L') # L = 8-bit pixels, black and white
img.show()

imgBits = cifrados.read_image(img)

I = cifrados.write_image(imgBits, img)
show_image(I)

# algorithms

# resultLGC_test = cifrados.lgc(a=3, b=3, N=7, seed=5, size=16) # Prueba de LGC retornando 16 bits
# print(resultLGC_test)
resultLGC = cifrados.lgc(a=15, b=2, N=7, seed=53, size=len(imgBits))

lgc_xor = cifrados.xor(imgBits, resultLGC)
print('xor')
print(resultLGC[:50])
print(imgBits[:50])
print(lgc_xor[:50])
show_image(cifrados.write_image(lgc_xor, img))

resultWichman = cifrados.wichman(134,1455,1132)
print(f"Wichman: {resultWichman}")