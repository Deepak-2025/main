import cv2
#import matplotlib.pyplot as plt
import cv2.data
import numpy as np

imagePath = 'face8.jpg'

img = cv2.imread(imagePath)
#gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("image dimensions:",img.shape)

#resizing the image according to their dimensions
if img.shape > (2000,2000,3):
    print("high quality image")
    height, width = img.shape[:2]
    new_dimensions = (width // 9, height // 9)
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_LINEAR)

elif img.shape < (2000 , 2000, 3) and img.shape > (1000, 1000, 3):
    print("mid quality image")
    height, width = img.shape[:2]
    new_dimensions = (width // 4, height // 4)
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_LINEAR)

elif img.shape > (500 , 500, 3) and img.shape < (1000, 1000, 3):
    print("low quality image")
    height, width = img.shape[:2]
    new_dimensions = (width // 2, height // 2)
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_LINEAR)

elif img.shape < (500 , 500, 3):
    print("provide better quality image")
    height, width = img.shape[:2]
    new_dimensions = (width * 2, height * 2)
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_LINEAR)


#resized_img = cv2.resize(img, (720, 480), interpolation=cv2.INTER_CUBIC)

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = face_classifier.detectMultiScale(resized_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


for (x, y, w, h) in faces:
    cv2.rectangle(resized_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the image with faces detected
cv2.imshow("Faces Detected", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




