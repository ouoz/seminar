from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import idou_heikin


img_name = "lena.pgm"
img_raw = Image.open(img_name)
img_gray = img_raw.convert('L')



img_in = np.array(img_raw)

plt.imshow(img_in)

img_out = idou_heikin.smooth(img_in, 5)

plt.imshow(img_out)
plt.gray()
plt.show()






"""
ad = 'lena.pgm'
img = Image.open(ad)

amp = 3

#一次微分による輪郭抽出
#img_out = gradient.gradient_difference(img, amp)
#img_out = gradient.gradient_roberts(img, amp)
#img_out = gradient.gradient_sobel(img, amp)

#Prewittの方法による輪郭抽出
img_out = prewitt.prewitt(img, amp)

#画像の二次微分
type = 1
#img_out = laplacian.laplacian(img, amp, type)

plt.imshow(img_out)
plt.gray()
plt.show()
"""