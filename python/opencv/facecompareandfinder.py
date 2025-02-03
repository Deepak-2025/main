import cv2
import face_recognition
import numpy as np
import os

imagePath = 'faces/face5.jpg'

# Load the image
img = cv2.imread(imagePath)
cv2.imshow("main",img)
cv2.waitKey(0)

# Print image dimensions
print("Image dimensions:", img.shape)

# Resizing the image according to its dimensions
if img.shape > (2000, 2000, 3):
    print("High quality image")
    height, width = img.shape[:2]
    new_dimensions = (width // 9, height // 9)
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_LINEAR)

elif img.shape < (2000, 2000, 3) and img.shape > (1000, 1000, 3):
    print("Mid quality image")
    height, width = img.shape[:2]
    new_dimensions = (width // 4, height // 4)
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_LINEAR)

elif img.shape > (500, 500, 3) and img.shape < (1000, 1000, 3):
    print("Low quality image")
    height, width = img.shape[:2]
    new_dimensions = (width // 2, height // 2)
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_LINEAR)

elif img.shape < (500 , 500, 3):
    print("provide better quality image")
    height, width = img.shape[:2]
    new_dimensions = (width * 2, height * 2)
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_LINEAR)

# Convert the image from BGR (OpenCV) to RGB (face_recognition)
rgb_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

# Use face_recognition to detect faces
face_locations = face_recognition.face_locations(rgb_img)

# Encoding known faces and their corresponding names
known_face_encodings = []
known_face_names = []

# Folder containing known face images
known_faces_folder = "faces"

naam = ['','white' ,'south indian','black','pink','brown','nothing','foreighner','korean','chinease','moon']


for i in range(1, 11):  # Looping for 20 faces
    try:
        # Load known face image (Ensure you have the images like 'face1.jpg', 'face2.jpg', ..., 'face20.jpg' in the folder)
        image_path = os.path.join(known_faces_folder, f"face{i}.jpg")
        known_image = face_recognition.load_image_file(image_path)
        
        # Get face encodings, ensure faces are found before proceeding
        encodings = face_recognition.face_encodings(known_image)
        
        if encodings:
            # If encodings are found, store the first encoding
            known_face_encoding = encodings[0]
            known_face_encodings.append(known_face_encoding)
            #known_face_names.append((f'person'[i]))
            known_face_names.append(naam[i]) # Assigning names as Person 1, Person 2, ...
            print('done')
            
        else:
            print(f"No faces found in {image_path}. Skipping.")
    
    except FileNotFoundError:
        print(f"Image for face{i} not found. Skipping.")

# Loop through each face found in the image
for (top, right, bottom, left) in face_locations:
    # Extract face encoding for the detected face
    face_encoding = face_recognition.face_encodings(rgb_img, [(top, right, bottom, left)])[0]

    # Compare the detected face with known faces
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    # If there's a match, use the name of the matching face
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
        print(name)

    # Draw a rectangle around the face and add the name
    cv2.rectangle(resized_img, (left, top), (right, bottom), (0, 255, 0), 2)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(resized_img, name, (left , bottom + 15), font, 0.5, (255, 255, 255), 1)

# Show the image with faces detected and names
cv2.imshow("Faces Detected", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
