import numpy as np
import math

def zero_cross(img): 
    img_out = np.zeros_like(img)

    h, w = img.shape

    for i in range(1, h - 1): 
        for j in range(1, w - 1): 
            if img[i][j] == 128:
                if (img[i][j + 1] - 128) * (img[i][j - 1] - 128) < 0: 
                    img_out[i][j] = 255
                if (img[i + 1][j] - 128) * (img[i - 1][j] - 128) < 0: 
                    img_out[i][j] = 255
                if (img[i + 1][j + 1] - 128) * (img[i - 1][j - 1] - 128) < 0: 
                    img_out[i][j] = 255
                if (img[i - 1][j + 1] - 128) * (img[i + 1][j - 1] - 128) < 0: 
                    img_out[i][j] = 255
            else:
                if (img[i][j] - 128) * (img[i - 1][j - 1] - 128) < 0: 
                    img_out[i][j] = 255
                if (img[i][j] - 128) * (img[i - 1][j] - 128) < 0: 
                    img_out[i][j] = 255
                if (img[i][j] - 128) * (img[i - 1][j + 1] - 128) < 0: 
                    img_out[i][j] = 255
                if (img[i][j] - 128) * (img[i][j - 1] - 128) < 0: 
                    img_out[i][j] = 255
    
    return img_out


def laplacian_of_gaussian(img, var, amp): 
    img_out = np.zeros_like(img)
    
    h, w = img.shape

    c = [[0.] * 51 for _ in range(51)]
    d = 0.
    r2 = 0.
    k = int(3 * 1.414 * var)
    if k > 25:
        k = 25
    v2 = var ** 2
    v4 = 1 / (v2 ** 2 * math.pi)
    
    for i in range(-k, k + 1):
        for j in range(-k, k + 1): 
            r2 = (i ** 2 + j ** 2) / v2 / 2
            c[25 + i][25 + j] = v4 * (r2 - 1) * math.exp(-r2)

    for i in range(0, h): 
        for j in range(0, w): 
            d = 128
            for u in range(-k, k + 1): 
                for v in range(-k, k + 1): 
                    y = i + u
                    x = j + v
                    if y < 0: 
                        y = 0
                    if x < 0:
                        y = 0
                    if y > h - 1: 
                        y = h - 1
                    if x > w - 1:
                        x = w - 1
                    d += c[25 + u][25 + v] * img[y][x]
            if d < 0: 
                d = 0
            if d > 255: 
                d = 255
            img_out[i][j] = int(d)
    
    return img_out


def log_zero_cross(img, var = 1.0, amp = 1.0): 
    h, w = img.shape

    img_LOG = laplacian_of_gaussian(img, var, amp)

    img_out = zero_cross(img_LOG)

    return img_out