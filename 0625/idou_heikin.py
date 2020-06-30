from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# img = 画像
# filter_size = フィルタのサイズ( = 3, 5, 7, 9, ....)
def smooth(img, filter_size): 
    h, w = img.shape
    num = filter_size ** 2
    k = filter_size // 2
    img_out = np.zeros_like(img).astype(np.float)

    for i in range(k, h - k):
        for j in range(k, w - k):
            sum = 0
            for u in range(-k, k + 1):
                for v in range(-k, k + 1):
                    sum += img[i + u][j + v]
            img_out[i][j] = sum // num

    img_out = img_out.astype(np.uint8)

    return img_out


def smooth_weighted(img): 
    filter = [[0.1, 0.1, 0.1],
              [0.1, 0.2, 0.1],
              [0.1, 0.1, 0.1]]

    img_out = np.zeros_like(img).astype(np.float)
    h, w = img.shape

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            sum = 0.0 
            for u in range(-1, 2): 
                for v in range(-1, 2): 
                    sum += img[i + u][j + v] * filter[u + 1][v + 1]
            img_out[i][j] = int(sum)
    
    img_out = img_out.astype(np.uint8)

    return img_out