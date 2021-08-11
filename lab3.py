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
from PIL import Image
import numpy as np

import PIL

result = cifrados.lgc(5, 3, 3, 7)
print(result)

cifrados.wichman(134,1455,1132)


#value = cifrados.read_image(img)



print('methot')
# load image as pixel array

img = Image.open('camera.png').convert('L')
img.show()
img = np.array(img)
print('fff',img.shape)
a = cifrados.read_image(img)
print('lennnn a ',len(a))
# summarize shape of the pixel array
print('greenasalfjks')
# display the array of pixels as an image
I = cifrados.write_image(a,img)
plt.figure()
plt.imshow(I,cmap='gray')
plt.show()

print('HERE')

'''def bits_to_int(bits):
    result = 0
    pot = 1
    for i in range(8):
        if (bits[7-i] == '1'):
            result += pow(2, pot)
        pot += 1
    return result'''

'''data = [ (bits_to_int(value[i:i+8])) for i in range(0, len(value), 8)]
data  = np.array(data)
data = data.reshape((img.size[1], img.size[0]))
im = PIL.Image.fromarray(np.uint8(data))
im.show()'''
#img = Image.new('RGB', (8, len(value)//8), "white")
#img.putdata(data)
#img.show()




#print(len(cifrados.read_image(img)))
print(cifrados.wichman(134,1455,1132))

#newImg = cifrados.write_image(img, result)







'''showImg = mpimg.imread(newImg)
imgplot = plt.imshow(showImg)


plt.show()'''
cifrados.wichman(134,1455,1132)