# -*- coding: utf-8 -*-
"""Single Face Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IMCR9dK7iFHSCt4AGTcjv8M6eSGsy1da
"""

import cv2
from google.colab.patches import cv2_imshow
import numpy as np

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the input image
input_image_path = '/mul-face.jpg'
input_image = cv2.imread(input_image_path)

# Convert the input image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Calculate the center of the input image
image_center = (input_image.shape[1] // 2, input_image.shape[0] // 2)

# Calculate the distance of each face from the center of the image and select the closest face
closest_face = None
closest_distance = float('inf')

for (x, y, w, h) in faces:
    # Calculate the center of the detected face
    face_center = (x + w // 2, y + h // 2)

    # Calculate the distance between the center of the image and the center of the face
    distance = np.sqrt((face_center[0] - image_center[0])**2 + (face_center[1] - image_center[1])**2)

    # Update the closest face if the current face is closer
    if distance < closest_distance:
        closest_face = (x, y, w, h)
        closest_distance = distance

# Draw a rectangle around the closest face in the input image
if closest_face is not None:
    (x, y, w, h) = closest_face
    cv2.rectangle(input_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(input_image, 'Closest Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Display the input image with the closest face highlighted
cv2_imshow( input_image)