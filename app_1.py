import streamlit as st
import torch
from diffusers import FluxPipeline
from PIL import Image
import io

# Initialize the pipeline
@st.cache_resource
def load_pipeline():
    return FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)

pipe = load_pipeline()

st.title("Image Generator with FLUX Pipeline")

# Text input from the user
prompt = st.text_input("Enter a prompt:", "A cat holding a sign that says hello world")

# Slider for guidance scale
guidance_scale = st.slider("Guidance Scale", min_value=1.0, max_value=10.0, value=3.5)

# Button to generate image
if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        # Generate image
        image = pipe(
            prompt,
            height=1024,
            width=1024,
            guidance_scale=guidance_scale,
            num_inference_steps=50,
            max_sequence_length=512,
            generator=torch.Generator("cpu").manual_seed(0)
        ).images[0]

        # Convert PIL Image to Bytes
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        # Display image
        st.image(buffer, caption="Generated Image", use_column_width=True)
