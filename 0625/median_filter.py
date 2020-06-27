from PIL import Image
import numpy as np


def smooth(img, filter_size): 
    img_out = np.zeros_like(img)
    h, w = img.shape
    k = filter_size // 2

    for i in range(k, h - k):
        for j in range(k, w - k):
            sum = 0
            window = []
            for u in range(-k, k + 1):
                for v in range(-k, k + 1):
                    window.append(img[i + u][j + v])
            window.sort()
            img_out[i][j] = window[(filter_size) ** 2 // 2]
    
    return img_out