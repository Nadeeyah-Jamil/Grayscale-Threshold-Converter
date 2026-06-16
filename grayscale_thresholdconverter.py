import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt

image = imread(r"/content/img.jpg")
print("image shape",image.shape)

Red=image[:,:,0]
#take all rows all cols and only 1 of channel
Green=image[:,:,1]
Blue=image[:,:,2]

grayscale=Red*0.2989+Green*0.587+0.114*Blue
print(grayscale.shape)

threeshold_value=128
threesholded=np.where(grayscale>threeshold_value,255,0)

plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.title("original")
plt.imshow(image.astype(np.uint8))

plt.subplot(1,3,2)
plt.title("Gray scale")
plt.imshow(grayscale,cmap="gray")

plt.subplot(1,3,3)
plt.title("Threeshold")
plt.imshow(threesholded,cmap="gray")

plt.tight_layout()
plt.show()
