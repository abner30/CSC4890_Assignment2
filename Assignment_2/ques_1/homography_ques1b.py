import cv2
import numpy as np
import matplotlib.pyplot as plt

src_points = np.array([[1842,1618],[3692,1693],[3663,2854],[1869,2549],[2709,2696]])
dest_points = np.array([[924,1646],[2744,1654],[2721,2701],[964,2651],[1896,2679]])

h, status = cv2.findHomography(src_points, dest_points)

im_src = cv2.imread('IMG_5055.png')
im_dst = cv2.imread('IMG_5054.png')

#-> this will give warped image output using h as homography matrix
im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

cv2.imshow("Warped_Source_Image", im_out)
plt.imshow(im_out)
plt.show()

print(h)

#homography matrix
#[[ 1.68719644e-01  2.60876523e-02  1.34357960e+03]
# [-2.12792802e-01  6.65053711e-01  3.60725030e+02]
# [-1.82383008e-04  3.38642018e-06  1.00000000e+00]]

#[[ 1.71252493e+00  1.78656727e-02 -1.98244246e+03]
#[ 2.19625662e-01  1.42263369e+00 -5.76816247e+02]
#[ 1.59975597e-04  1.62684501e-06  1.00000000e+00]]


