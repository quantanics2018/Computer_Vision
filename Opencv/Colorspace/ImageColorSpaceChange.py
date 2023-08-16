import cv2

# Load an image in BGR format
image = cv2.imread(r"D:\OpenCV\Colorspace\orange.jpg")

# Convert BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
