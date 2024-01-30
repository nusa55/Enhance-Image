import streamlit as st
from PIL import Image, ImageEnhance

def enhance_image(image, enhancement_factor):
    enhanced_image = enhance_image = ImageEnhance.Contrast(image).enhance(enhancement_factor)
    return (enhanced_image)

def main():
    st.title('Enhance Your Image')
    st.write('Upload an image and enhance it!')

    uploade_image = st.file_uploader("Choose a image...", type=["jpg", "jpeg", "png"])

    if uploade_image is not None:
        st.image(uploade_image, caption='Original Image',use_column_width=True)

        enhancement_factor = st.slider('Enhancement Factor', 0.0, 2.0, 1.0)

        if st.button('Enhance'):
            # Load the image
            img = Image.open(uploade_image)

            # Enhance the image
            enhanced_img = enhance_image(img, enhancement_factor)
            st.image(enhanced_img, caption='Enhanced Image', use_column_width=True)

if __name__ == "__main__":
    main()