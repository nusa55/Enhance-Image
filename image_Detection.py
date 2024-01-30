import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image

# Function to perform object detection on an image
def detect_objects(image):
    image_np = np.array(image)
    converted_img = tf.image.convert_image_dtype(image_np, tf.float32)[tf.newaxis, ...]

    result = model(converted_img)

    result = {key: value.numpy() for key, value in result.items()}
    num_detections = int(result.pop('num_detections'))
    result = {key: value[:num_detections] for key, value in result.items()}
    result['num_detections'] = num_detections

    return result

# Streamlit app
def main():
    st.title("Object Detection App")
    st.write("Upload an image and detect objects!")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)

        # Perform object detection
        detections = detect_objects(image)

        # Display the detected objects
        st.write("Detected Objects:")
        for i in range(detections['num_detections']):
            st.write(f"- {detections['detection_classes'][i]}: {detections['detection_scores'][i]}")

        # Display the image with bounding boxes around the detected objects
        st.image(image, caption='Detected Objects', use_column_width=True, channels="RGB")

if __name__ == "__main__":
    main()
