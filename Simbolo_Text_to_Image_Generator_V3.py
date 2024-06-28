import streamlit as st
import requests
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/Aungkhine/Simbolo_Text_to_Image_Generator_V3"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #cfe2f3;
        color: white;
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        color: #f9c74f;
        margin-bottom: 20px;
    }
    .description {
        text-align: center;
        font-size: 1.2rem;
        color: #f9c74f;
        margin-bottom: 20px;
    }
    .input-box {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .input-field {
        width: 60%;
        padding: 10px;
        border: 1px solid #f9c74f;
        border-radius: 5px;
        background-color: #2d2d2d;
        color: white;
    }
    .generate-btn {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #8c8c8c;
        margin-top: 40px;
    }
    .spinner {
        color: #f9c74f;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page title
st.markdown("<div class='title'>Simbolo 'Happy' Fine Tuned Text to Image Generator</div>", unsafe_allow_html=True)
st.markdown("<div class='description'>This model is a fine-tuned version of the Stable Diffusion model, specifically designed to generate images of 'Happy', the representative character of Simbolo, an IT class in Myanmar.</div>", unsafe_allow_html=True)

# Input field
st.markdown("<div class='input-box'><input class='input-field' type='text' id='description' value='Make sure your prompt must include Simbolo'></div>", unsafe_allow_html=True)
user_input = st.text_input("Enter your prompt here:", "A photo of Simbolo, reading an IT Book.")

if st.button("Generate"):
    with st.spinner("Generating image..."):
        response = query({"inputs": user_input})
        if response.status_code == 200:
            try:
                image_bytes = response.content
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption=user_input)
            except Exception as e:
                st.error(f"Error generating image: {e}")
        else:
            st.error(f"API request failed with status code {response.status_code}: {response.text}")

# Footer
st.markdown("<div class='footer'>Developed with ❤️ by Team Zee Kwat</div>", unsafe_allow_html=True)
