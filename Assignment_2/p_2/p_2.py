import numpy as np
import cv2

imgPath=["/Users/abno2018/depthai/ass2/p_2/Test1/testL.jpg","/Users/abno2018/depthai/ass2/p_2/Test1/testC.jpg","/Users/abno2018/depthai/ass2/p_2/Test1/testR.jpg"]

imgPath2=["/Users/abno2018/depthai/ass2/p_2/Test2/bookstore1.jpg","/Users/abno2018/depthai/ass2/p_2/Test2/bookstore2.jpg","/Users/abno2018/depthai/ass2/p_2/Test2/bookstore3.jpg"]

imgPath3=["/Users/abno2018/depthai/ass2/p_2/Test3/bookstore5.jpg","/Users/abno2018/depthai/ass2/p_2/Test3/bookstore6.jpg","/Users/abno2018/depthai/ass2/p_2/Test3/bookstore7.jpg"]

imgPath4=["/Users/abno2018/depthai/ass2/p_2/Test4/sc1.jpg","/Users/abno2018/depthai/ass2/p_2/Test4/sc2.jpg","/Users/abno2018/depthai/ass2/p_2/Test4/sc3.jpg"]

imgPath5=["/Users/abno2018/depthai/ass2/p_2/Test5/ul1.jpg","/Users/abno2018/depthai/ass2/p_2/Test5/ul2.jpg","/Users/abno2018/depthai/ass2/p_2/Test5/ul3.jpg"]

images = []

for path in imgPath5:
	image = cv2.imread(path)
	images.append(image)

print(len(images))
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
	print("Image Stitching Successful")
	cv2.imshow("Stitched Image", stitched)
	cv2.waitKey(0)
else:
	print("[INFO] Failed Image Stitching ({})"/format(status))
