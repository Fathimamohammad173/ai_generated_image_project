import streamlit as st
from utils.generation import generate_image

st.title("AI Text-to-Image Generator (Open-Source)")

prompt = st.text_input("Enter your prompt")
negative = st.text_input("Negative prompt", "low quality, blurry, distorted")
num_images = st.slider("Number of Images", 1, 4, 1)
steps = st.slider("Inference Steps", 10, 50, 25)
guidance = st.slider("Guidance Scale", 1.0, 15.0, 7.5)

if st.button("Generate"):
    with st.spinner("Generating..."):
        images = generate_image(prompt, negative, num_images, steps, guidance)
        for i, img in enumerate(images):
            st.image(img)
            img.save(f"outputs/images/{datetime.now().timestamp()}_{i}.png")
