import streamlit as st
import cv2
import numpy as np

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in the image
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return image

# Streamlit app
def main():
    st.title("Image Detection App")
    st.write("Upload an image and detect faces!")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Perform face detection
        detected_image = detect_faces(image)

        # Display the original and detected images
        st.image(image, channels="BGR", caption="Original Image", use_column_width=True)
        st.image(detected_image, channels="BGR", caption="Detected Faces", use_column_width=True)

if __name__ == "__main__":
    main()
