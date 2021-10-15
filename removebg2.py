# Auto detect text files and perform LF normalization
* text=auto

import cv2
import numpy as np
from matplotlib import pyplot as plt

image bgr = cv2.imread('images/imput 2.jpg')
image_rgh = cv2.cvtColor (images_bgr, cv2.COLOR_BGR2RGB)

rectangle = (0, 0, 300, 380)

mask = np.zeros (image_rgb.shape [:2]), np.unint8)

bgdModel = np.zeros ((1, 65), np.float64)
fgdModel = np.zeros ((1, 65), np.float64)

cv2.grabCut (image_rgb, mask, rectangle, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask_2 = np.where ((mask == 2) ∣ (mask == 0), 0, 1).astype ('uint8') 

image_rgd_nobg = image_rgb * mask_2[:, :, np.newaxis] 

plt.imshow (image_rgd_nobg), plt.axis ('off')
plt.show()