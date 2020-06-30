import copy
import numpy as np


def average_minv(p): 
    ave = [0.] * 9
    var = [0.] * 9
    dmin = 0.

    for k in range(8):
        for i in range(7):
            ave[k] += p[k][i]
        ave[k] /= 7
        for i in range(7): 
            var[k] += (p[k][i] - ave[k]) ** 2
        var[k] /= 7
    
    for i in range(9): 
        ave[k] += p[k][i]
    ave[8] /= 9
    for i in range(9): 
        var[8] += (p[8][i] - ave[8]) ** 2
    var[8] /= 9

    mini = 0
    for k in range(9): 
        if dmin > var[k]: 
            dmin = var[k]
            mini = k

    return ave[mini]

def smooth(img): 
    patx = [[0, -1,  0,  1, -1,  0,  1,  0,  0],
            [0,  1,  2,  0,  1,  2,  1,  0,  0],
            [0,  1,  2,  1,  2,  1,  2,  0,  0],
            [0,  1,  0,  1,  2,  1,  2,  0,  0],
            [0, -1,  0,  1, -1,  0,  1,  0,  0],
            [0, -1, -2, -1,  0, -2, -1,  0,  0],
            [0, -2, -1, -2, -1, -2, -1,  0,  0],
            [0, -2, -1, -2, -1,  0, -1,  0,  0],
           [-1,  0,  1, -1,  0,  1, -1,  0,  1]]
    
    paty = [[0, -2, -2, -2, -1, -1, -1,  0,  0],
            [0, -2, -2, -1, -1, -1,  0,  0,  0],
            [0, -1, -1,  0,  0,  1,  1,  0,  0],
            [0,  0,  1,  1,  1,  2,  2,  0,  0],
            [0,  1,  1,  1,  2,  2,  2,  0,  0],
            [0,  0,  1,  1,  1,  2,  2,  0,  0],
            [0, -1, -1,  0,  0,  1,  1,  0,  0],
            [0, -2, -2, -1, -1, -1,  0,  0,  0],
           [-1, -1, -1,  0,  0,  0,  1,  1,  1]]
    
    h, w = img.shape

    img_out = np.zeros_like(img).astype(np.float)

    p = [[0] * 9 for _ in range(9)]
    
    for i in range(2, h - 2):
        for j in range(2, w - 2): 
            for u in range(0, 9): 
                for v in range(0, 9): 
                    p[u][v] = img[i + paty[u][v]][j + patx[u][v]]
            img_out[i][j] = average_minv(p)
    
    img_out = img_out.astype(np.uint8)

    return img_out