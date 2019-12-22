# NILATIL MOENA (1313618002)
# Ilmu Komputer 2018
# Assignment 5

# Implementation of: Watershed algorithm
# Algoritma mampu mendeteksi tepi

# Python Imaging Library/ PIL
# mendukungan untuk membuka, memanipulasi, dan menyimpan banyak format file image/gambar yang berbeda. 
from PIL import Image
# libraries dari skimage
from skimage import measure
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import sobel
import matplotlib.pyplot as plt

# Untuk image
# Menemukan image yang akan diproses dengan 'nama image.format image'
img = Image.open("dolphin.jpg")
# Menampilkan image
img.show()

# Membaca image
img = imread("dolphin.jpg")

# Mengubah RGB menjadi grayscale
img_gray = rgb2gray(img)

# Fungsi sobel untuk menemukan tepi image
img_edges = sobel(img_gray)

# Menemukan contour pada image
contours = measure.find_contours(img_edges, 0.2)

# Menampilkan gambar 
fig, ax = plt.subplots()
ax.imshow(img_edges, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])

# Menampilkan hasil image
plt.show()
