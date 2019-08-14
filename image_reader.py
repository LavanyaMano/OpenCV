import cv2, time


# img = cv2.imread("image1.jpg",1)


# print(img.shape)

# cv2.imshow("image",img)

# cv2.waitKey(0)

# cv2.destroyAllWindows()

# resized = cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))

# cv2.imshow("imageResized",resized)

# cv2.waitKey(0)

# cv2.destroyAllWindows()


video = cv2.VideoCapture(0)




a=1
while True:
	a = a+1

# time.sleep(5)
	check, frame = video.read()

	print(check)

	print(frame)

	cv2.imshow('capture',frame)

	key = cv2.waitKey(1)

	if key== ord('a'):
		break

print("number of frames  ==>  ",a)


video.release()

cv2.destroyAllWindows()