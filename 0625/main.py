from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import idou_heikin
import noise
import median_filter
import edge_preserve
import LOG
import binary


img_name = "lena.pgm"
img_raw = Image.open(img_name)
img_gray = img_raw.convert('LA')



#原画像読み込み
img_in = np.array(img_raw)
h, w = img_in.shape

#画像のクリッピング
img_in = np.array([img_in[i][120: 250] for i in range(h // 4)])

plt.gray()

plt.subplot(1, 5, 1)
plt.imshow(img_in)


"""
# 移動平均フィルタ

img_ave = idou_heikin.smooth(img_in, 11)

plt.subplot(1, 5, 2)
plt.imshow(img_ave)
plt.show()
"""

#ノイズ付加
img_noised = noise.noise(img = img_in, noise_range = 32)

plt.subplot(1, 5, 2)
plt.imshow(img_noised)

"""
#重み付き移動平均フィルタ
img_ave_w = idou_heikin.smooth_weighted(img = img_in)

plt.subplot(1, 5, 3)
plt.imshow(img_ave_w)
"""

"""
#メディアンフィルタ
img_med = median_filter.smooth(img = img_noised, filter_size = 3)

plt.subplot(1, 5, 3)
plt.imshow(img_med)
"""


"""
#スパイクノイズ
img_spiked = noise.noise_spike(img = img_in, noise_range = 32, number = h * w)
plt.subplot(1, 5, 3)
plt.imshow(img_spiked)
"""



"""
#エッジ保存平滑化
img_out = edge_preserve.smooth(img_noised)
plt.subplot(1, 5, 3)
plt.imshow(img_out)
"""


#LOGフィルタ -> ゼロ交差エッジ抽出
img_log = LOG.log_zero_cross(img_noised, var = 2.5)
plt.subplot(1, 5, 3)
plt.imshow(img_log)




#膨張処理(2値画像)

img_out = binary.dilation(img_log)
plt.subplot(1, 5, 4)
plt.imshow(img_out)


#収縮処理(2値画像)
img_out = binary.erosion(img_out)
plt.subplot(1, 5, 5)
plt.imshow(img_out)


plt.show()


