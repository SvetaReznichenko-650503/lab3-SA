from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
import scipy.stats as st

img1 = Image.open('pic1.jpg').convert('LA')
img1.save('greyscale1.png')
img2 = Image.open('pic2.jpg').convert('LA')
img2.save('greyscale2.png')

img = cv2.imread('greyscale2.png')
b,g,r = cv2.split(img)
fig = plt.figure(figsize=(8,4))

ax = fig.add_subplot(121)
ax.imshow(img[...,::-1])

ax = fig.add_subplot(122)
for x, c in zip([b,g,r], ["b", "g", "r"]):
    xs = np.arange(256)
    ys = cv2.calcHist([x], [0], None, [256], [0,256])
    ax.plot(xs, ys.ravel(), color=c)

ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()
