import numpy as np

# Linear congruential generator
# seed, a, b, N and size must be positive int values
def lgc(a, b, N, seed, size):
  k = 1 # ultimos bits a tomar
  t = int(size / k) # cantidad de iteraciones
  h = seed
  cadena = ''
  for _ in range(t):
    bits = format(((a * h) + b) % N, '08b')
    h = ((a * h) + b) % N
    cadena += bits[-k:]
  return cadena

# Wichman-Hill generator
def wichman(s1,s2,s3,size):
  k = 1
  t = int(size/k)
  s = ''
  for _ in range(t):
    s1 = (171*s1) % 30269
    s2 = (172*s2) % 30307
    s3 = (170*s3) % 30323

    v = (s1/30269.0 + s2/30307.0 + s3/30323.0) %1
    s += format(int(v*1e15),'08b')[-k:]
  return s


# converts image to bits
# receives an opened PIL image on "L" mode (8 bits)
# returns a full string of bits
def read_image(image):
  image = np.array(image)
  width, height = image.shape
  bits = ""
  for i in range(0,width):
    for j in range(0,height):
      bits += '{0:08b}'.format(image[i,j])
  return bits

# converts bits to image
# receives a full string of bits
# returns a numpy array with 8 bits values per pixel
def write_image(bits, image):
  imgArray = np.empty(int(len(bits)/8), dtype=np.uint8)
  for i in range(int(len(bits)/8)):
    imgArray[i] = int(bits[(i*8):(i*8)+8], 2)
  img = imgArray.reshape(np.array(image).shape)
  return img

# xor two strings of bits
# returns a string of bits
def xor(bits1, bits2):
  return ''.join(str(int(bits1[i]) ^ int(bits2[i])) for i in range(len(bits1)))
