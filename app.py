# import streamlit as st
# import requests
# from PIL import Image
# import io

# # Constants for the API
# API_URL = "https://api-inference.huggingface.co/models/XLabs-AI/flux-RealismLora"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     response.raise_for_status()  # Raise an error if the request failed
#     return response.content

# st.title("Image Generator with FLUX Pipeline")

# # Text input from the user
# prompt = st.text_input("Enter a prompt:", "Astronaut riding a horse")

# # Slider for guidance scale
# guidance_scale = st.slider("Guidance Scale", min_value=1.0, max_value=10.0, value=3.5)

# # Button to generate image
# if st.button("Generate Image"):
#     with st.spinner("Generating image..."):
#         try:
#             # Query the API
#             image_bytes = query({
#                 "inputs": prompt,
#                 "parameters": {
#                     "guidance_scale": guidance_scale,
#                     "num_inference_steps": 50,
#                     "max_sequence_length": 512
#                 }
#             })

#             # Convert image bytes to PIL Image
#             image = Image.open(io.BytesIO(image_bytes))

#             # Display image
#             st.image(image, caption="Generated Image", use_column_width=True)
#         except requests.exceptions.RequestException as e:
#             st.error(f"Error generating image: {e}")
#         except Exception as e:
#             st.error(f"An unexpected error occurred: {e}")

import streamlit as st
import requests
from PIL import Image
import io
import base64

# Set page config
st.set_page_config(page_title="FLUX AI Image Creator", page_icon="🎨", layout="wide")

# Modern and premium CSS enhancements
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    :root {
        --primary-bg: #121212;
        --secondary-bg: #1E1E1E;
        --accent-1: #3B82F6;
        --accent-2: #EF4444;
        --text-color: #E0E0E0;
        --highlight: #F59E0B;
    }

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        color: var(--text-color);
    }

    .stApp {
        background-color: var(--primary-bg);
        display: flex;
        flex-direction: column;
        padding: 20px;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Sleek Header */
    h1 {
        color: var(--text-color);
        font-weight: 700;
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
        transition: all 0.4s ease;
        text-shadow: 1px 1px 8px rgba(0, 0, 0, 0.5);
    }

    h1:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.5);
    }

    /* Input and Button Styles */
    .stTextInput > div > div > input {
        background-color: var(--secondary-bg);
        color: var(--text-color);
        border: 1px solid var(--accent-1);
        border-radius: 8px;
        padding: 10px;
        transition: all 0.3s ease;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--highlight);
        box-shadow: 0 0 10px var(--highlight);
    }

    .stButton > button {
        background: var(--accent-1);
        color: var(--text-color);
        border-radius: 20px;
        padding: 10px 24px;
        font-weight: 600;
        border: none;
        transition: background 0.3s ease, transform 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }

    .stButton > button:hover {
        background: var(--accent-2);
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
    }

    /* Image Box */
    .image-box {
        background: rgba(30, 30, 30, 0.85);
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-top: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .image-box:hover {
        transform: scale(1.03);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
    }

    /* Sleek Footer */
    .footer {
        text-align: center;
        padding: 15px 0;
        background: var(--secondary-bg);
        border-top: 1px solid var(--accent-1);
        color: var(--text-color);
        margin-top: 3rem;
        box-shadow: 0 -3px 15px rgba(0, 0, 0, 0.2);
        border-radius: 8px;
        animation: fadeInUp 0.8s ease-out;
    }

    .footer p {
        margin: 0;
        font-size: 14px;
        font-weight: 400;
        letter-spacing: 0.5px;
    }

    .footer p:hover {
        color: var(--highlight);
        transition: color 0.3s ease;
    }

    /* Animations */
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
</style>




""", unsafe_allow_html=True)

# Helper function for API call
def query(payload, model_choice):
    if model_choice == "FLUX RealismLora":
        API_URL = "https://api-inference.huggingface.co/models/XLabs-AI/flux-RealismLora"
        headers = {"Authorization": "Bearer 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"}
    else:  # FLUX.1-schnell
        API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
        headers = {"Authorization": "Bearer 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"}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.content

# Main content
st.markdown("<h1>FLUX AI Image Creator</h1>", unsafe_allow_html=True)

# Centered content layout
st.markdown("<div style='display: flex; justify-content: center; align-items: center; flex-direction: column;'>", unsafe_allow_html=True)

# Image generation settings
model_choice = st.selectbox(
    "Choose AI Model",
    ("FLUX RealismLora", "FLUX.1-schnell"),
    index=0
)

prompt = st.text_input("Enter your prompt:", "A futuristic cityscape with flying cars")

guidance_scale = st.slider("Creativity Level", min_value=1.0, max_value=10.0, value=7.5, step=0.1)
num_inference_steps = st.slider("Image Quality", min_value=20, max_value=100, value=50, step=5)

if st.button("🎨 Generate Image"):
    with st.spinner("🚀 Creating your masterpiece..."):
        try:
            image_bytes = query({
                "inputs": prompt,
                "parameters": {
                    "guidance_scale": guidance_scale,
                    "num_inference_steps": num_inference_steps,
                    "max_sequence_length": 100
                }
            }, model_choice)
            
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width="auto")

            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            # Download button
            st.download_button(
                label="Download Image",
                data=base64.b64decode(img_str),
                file_name="flux_generated_image.png",
                mime="image/png",
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Closing centered content layout
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>© 2024 FLUX AI. All Rights Reserved.</div>", unsafe_allow_html=True)
