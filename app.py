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
st.set_page_config(page_title="Text-2-Image Generator", page_icon="🎨", layout="wide")


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

    :root {
        --primary-bg: #0A0A0A;
        --secondary-bg: #1A1A1A;
        --accent-1: #6E56CF;
        --accent-2: #C24BF6;
        --text-color: #E0E0E0;
        --highlight: #9F7AEA;
        --muted: #6B7280;
        --divider: #2D2D2D;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text-color);
        background-color: var(--primary-bg);
    }

    .stApp {
        background: linear-gradient(135deg, var(--primary-bg), var(--secondary-bg));
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
        margin: 0 auto;
    }

    /* Sleek Header */
    h1 {
        color: var(--text-color);
        font-weight: 600;
        text-align: center;
        padding: 40px 0;
        font-size: 48px;
        letter-spacing: -0.015em;
        margin-bottom: 2rem;
        background: linear-gradient(45deg, var(--accent-1), var(--accent-2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 8s ease infinite;
    }

    /* Input and Button Styles */
    .stTextInput > div > div > input {
        background-color: var(--secondary-bg);
        color: var(--text-color);
        border: 1px solid var(--muted);
        border-radius: 8px;
        padding: 12px 16px;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--accent-1);
        box-shadow: 0 0 0 2px rgba(110, 86, 207, 0.25);
    }

    .stButton > button {
        background: linear-gradient(45deg, var(--accent-1), var(--accent-2));
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 14px;
    }

    .stButton > button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(159, 122, 234, 0.3);
    }

    /* Radio Button Styles */
    .stRadio > div {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 20px;
    }

    .stRadio > div > label {
        cursor: pointer;
        display: flex;
        align-items: center;
        background-color: var(--secondary-bg);
        border: 1px solid var(--muted);
        border-radius: 8px;
        padding: 10px 15px;
        transition: all 0.3s ease;
    }

    .stRadio > div > label:hover {
        border-color: var(--accent-1);
    }

    .stRadio > div > label > div {
        font-size: 16px;
        font-weight: 500;
        margin-left: 10px;
    }

    /* Slider Styles */
    .stSlider > div > div > div {
        background-color: var(--accent-1);
    }

    .stSlider > div > div > div > div {
        background-color: var(--accent-2);
        border: 2px solid var(--accent-1);
    }

    /* Image Box */
    .image-box {
        background: rgba(26, 26, 26, 0.6);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 30px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .image-box:hover {
        transform: scale(1.02);
        box-shadow: 0 12px 48px rgba(0, 0, 0, 0.3);
    }

    /* Sleek Footer */
    .footer {
        text-align: center;
        padding: 20px 0;
        color: var(--muted);
        margin-top: 3rem;
        font-size: 14px;
        font-weight: 400;
    }

    /* Animations */
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        animation: fadeIn 0.8s ease-out;
    }

    /* New styles for enhanced structure */
    .section {
        background: var(--secondary-bg);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid var(--divider);
    }

    .section-title {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 15px;
        color: var(--accent-1);
    }

    .divider {
        height: 1px;
        background-color: var(--divider);
        margin: 20px 0;
    }

    .label {
        font-size: 14px;
        color: var(--muted);
        margin-bottom: 5px;
    }

    .value {
        font-size: 16px;
        color: var(--text-color);
        background: rgba(110, 86, 207, 0.1);
        padding: 8px 12px;
        border-radius: 6px;
        margin-bottom: 15px;
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
st.markdown("<h1>Text-2-Image Generator</h1>", unsafe_allow_html=True)

# Image generation settings
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Model Selection</div>', unsafe_allow_html=True)
model_choice = st.radio(
    "Choose AI Model",
    ("FLUX RealismLora", "FLUX.1-schnell"),
    index=0
)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Image Prompt</div>', unsafe_allow_html=True)
prompt = st.text_input("Enter your prompt", value="A futuristic cityscape with flying cars")


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Generation Parameters</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    guidance_scale = st.slider("Creativity Level", min_value=1.0, max_value=10.0, value=7.5, step=0.1)
with col2:
    num_inference_steps = st.slider("Image Quality", min_value=20, max_value=100, value=50, step=5)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

if st.button("Generate Image"):
    with st.spinner("Creating your masterpiece..."):
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
            st.markdown('<div class="section">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">Generated Image</div>', unsafe_allow_html=True)
            st.markdown('<div class="image-box">', unsafe_allow_html=True)
            st.image(image, caption="", use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Display generation parameters
            st.markdown('<div class="label">Prompt</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="value">{prompt}</div>', unsafe_allow_html=True)
            st.markdown('<div class="label">Model</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="value">{model_choice}</div>', unsafe_allow_html=True)
            st.markdown('<div class="label">Creativity Level</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="value">{guidance_scale}</div>', unsafe_allow_html=True)
            st.markdown('<div class="label">Image Quality</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="value">{num_inference_steps}</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

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

# Footer
st.markdown("<div class='footer'>© 2024. All Rights Reserved.</div>", unsafe_allow_html=True)