from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# img = 画像
# filter_size = フィルタのサイズ( = 3, 5, 7, 9, ....)
def smooth(img, filter_size): 
    h, w = img.shape
    num = filter_size ** 2
    k = filter_size // 2
    img_out = np.zeros_like(img)

    for i in range(k, h - k):
        for j in range(k, w - k):
            sum = 0
            for u in range(-k, k + 1):
                for v in range(-k, k + 1):
                    sum += img[i + u][j + v]
            img_out[i][j] = sum // num

    return img_out