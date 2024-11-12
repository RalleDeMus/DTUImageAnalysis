import matplotlib.pyplot as plt
import skimage.io as io

src_img = io.imread("data/Hand2.jpg")

plt.imshow(src_img)
plt.show()