from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("img.jpg")  
img_array = np.array(img)      

red = img_array[:, :, 0]
green = img_array[:, :, 1]
blue = img_array[:, :, 2]

hist_red, bins = np.histogram(red, bins=256, range=(0, 255))
hist_green, bins = np.histogram(green, bins=256, range=(0, 255))
hist_blue, bins = np.histogram(blue, bins=256, range=(0, 255))

plt.figure(figsize=(10, 4))
plt.plot(hist_red, color='red', label='Red')
plt.plot(hist_green, color='green', label='Green')
plt.plot(hist_blue, color='blue', label='Blue')
plt.title("RGB Histogram")
plt.xlabel(" value (0-255)")
plt.ylabel("num of pixels ")
plt.legend()
plt.show()
