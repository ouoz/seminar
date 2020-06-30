import numpy as np


def dilation(img): 
    img_out = np.zeros_like(img).astype(np.float)

    h, w = img_out.shape

    for i in range(1, h - 1): 
        for j in range(1, w - 1): 
            img_out[i][j] = img[i][j]
            if img[i - 1][j - 1] == 255:
                img_out[i][j] = 255
            if img[i - 1][j] == 255:
                img_out[i][j] = 255
            if img[i - 1][j + 1] == 255:
                img_out[i][j] = 255
            if img[i][j - 1] == 255:
                img_out[i][j] = 255
            if img[i][j + 1] == 255:
                img_out[i][j] = 255
            if img[i + 1][j - 1] == 255:
                img_out[i][j] = 255
            if img[i + 1][j] == 255:
                img_out[i][j] = 255
            if img[i + 1][j + 1] == 255:
                img_out[i][j] = 255
    
    img_out = img_out.astype(np.uint8)

    return img_out


def erosion(img): 
    img_out = np.zeros_like(img).astype(np.float)

    h, w = img.shape

    for i in range(1, h - 1): 
        for j in range(1, w - 1): 
            img_out[i][j] = img[i][j]
            if img[i - 1][j - 1] == 0:
                img_out[i][j] = 0
            if img[i - 1][j] == 0:
                img_out[i][j] = 0
            if img[i - 1][j + 1] == 0:
                img_out[i][j] = 0
            if img[i][j - 1] == 0:
                img_out[i][j] = 0
            if img[i][j + 1] == 0:
                img_out[i][j] = 0
            if img[i + 1][j - 1] == 0:
                img_out[i][j] = 0
            if img[i + 1][j] == 0:
                img_out[i][j] = 0
            if img[i + 1][j + 1] == 0:
                img_out[i][j] = 0

    img_out = img_out.astype(np.unit8)

    return img_out