import cv2
import streamlit as st
import numpy as np
from datetime import datetime

def detect_objects(image, cascade_files):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    objects = []

    for cascade_path in cascade_files:
        # Load pre-trained object detection model (e.g., using Haar cascades)
        cascade = cv2.CascadeClassifier(cascade_path)

        # Perform object detection
        detected_objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        objects.extend(detected_objects)

    return objects

def draw_objects(image, objects):
    # Draw rectangles around the detected objects
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image

def main():
    st.title("Object Detection with Time Display")

    # Define the available object types for detection
    object_types = {
        "Cars": ["cars.xml"],
        "Humans": ["human.xml"],
        "Bus": ["bus.xml"]
    }

    # Sidebar object type selection
    object_type = st.sidebar.selectbox("Select the object type", list(object_types.keys()))

    # Display the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    st.subheader("Current Time")
    st.write(current_time)

    # File upload
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Perform object detection based on selected object type
        cascade_files = object_types[object_type]
        objects = detect_objects(image, cascade_files)

        # Draw rectangles around the detected objects
        output_image = draw_objects(image.copy(), objects)

        # Display the original and processed images
        st.subheader("Original Image")
        st.image(image, channels="BGR")

        st.subheader("Detected Objects")
        st.image(output_image, channels="BGR")

        # Display the number of detected objects
        st.write("Number of Detected Objects:", len(objects))

if __name__ == "__main__":
    main()
