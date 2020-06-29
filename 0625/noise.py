from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random
import copy


def noise(img, noise_range = 32): 
    img_out = np.zeros_like(img)
    h, w = img.shape
    
    for i in range(h):
        for j in range(w): 
            noise = random.randint(-noise_range, noise_range)
            pix = img[i][j] + noise
            if pix > 255: 
                pix = 255
            elif pix < 0:
                pix = 0
            img_out[i][j] = pix

    return img_out


def noise_spike(img, number = 1000, noise_range = 32):
    img_out = copy.deepcopy(img)
    h, w = img.shape
    
    for _ in range(number): 
        y = random.randint(0, h - 1)
        x = random.randint(0, w - 1)
        noise = random.randint(-noise_range, noise_range)
        pix = img_out[y][x] + noise
        if pix > 255: 
            pix = 255
        elif pix < 0:
            pix = 0
        img_out[y][x] = pix
    
    return img_out
