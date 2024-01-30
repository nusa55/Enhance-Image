import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Load the pre-trained COCO-SSD model
model = hub.load("https://tfhub.dev/tensorflow/coco-ssd/1")

# Function to perform object detection on an image
def detect_objects(image_path):
    image = Image.open(image_path)
    image_np = np.array(image)
    converted_img  = tf.image.convert_image_dtype(image_np, tf.float32)[tf.newaxis, ...]

    result = model(converted_img)

    result = {key: value.numpy() for key, value in result.items()}
    num_detections = int(result.pop('num_detections'))
    result = {key: value[:num_detections] for key, value in result.items()}
    result['num_detections'] = num_detections

    return result

# Example usage:
image_path = 'path/to/your/image.jpg'  # Replace with the path to your image
detections = detect_objects(image_path)
print(detections)
