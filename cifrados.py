import numpy as np
import re
#solo la ultima parte TODO
def lgc(seed, a, b, N):
  t = 10
  k = format(seed, '08b')
  h = seed
  if (N > 0):
    for i in range(1, t):
      bits = format((a * h + b) % N, '08b')
      h = (a * h + b) % N
      k += bits
    return k
  else:
    print("N debe ser positivo")

# read image to bits
# returns a full string of bits
def read_image(image):
  width, height = image.shape
  bits = ""
  for i in range(0,width):
    for j in range(0,height):
      bits += '{0:08b}'.format(image[i,j])
  return bits

# bits to image
# receives a string of bits
# returns a new image
def write_image(bits, image):

  width, height= image.shape
  I = np.zeros(width*height).astype(np.uint8)
  bts = re.findall('.........',bits)

  for i in range(0,len(bts)):
    I[i] = int(bts[i],2)

  I  = I.reshape((width, height))

  return I

def wichman(s1,s2,s3):
  t = 10
  s = ''
  for i in range(1,t):
    s1 = (171*s1) % 30269
    s2 = (172*s2) % 30307
    s3 = (170*s3) % 30323

    v = (s1/30269.0 + s2/30307.0 + s3/30323.0) %1
    s += format(int(v*1e15),'08b')[-8:]
  return s




