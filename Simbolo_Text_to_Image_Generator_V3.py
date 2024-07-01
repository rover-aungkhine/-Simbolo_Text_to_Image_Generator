import streamlit as st
import requests
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/Aungkhine/Simbolo_Text_to_Image_Generator_V3"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 503:
            st.error("The model is currently loading. Please try again in a few moments.")
        else:
            st.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        st.error(f"An error occurred: {err}")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000; /* Slightly lighter background */
        color: #000000; /* White text */
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        color: #ffcc00; /* Bright yellow for title */
        margin-bottom: 20px;
    }
    .description {
        text-align: center;
        font-size: 1.2rem;
        color: #ffcc00; /* Bright yellow for description */
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
        border: 1px solid #ffcc00; /* Bright yellow border */
        border-radius: 5px;
        background-color: #3c3c3c; /* Darker input background */
        color: #ffffff; /* White text */
    }
    .generate-btn {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .generate-btn button {
        background-color: #ff4d4d; /* Bright red button */
        color: #ffffff; /* White text */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 1rem;
        cursor: pointer;
    }
    .generate-btn button:hover {
        background-color: #e60000; /* Darker red on hover */
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #ffffff; /* Light gray for footer */
        margin-top: 40px;
    }
    .spinner {
        color: #ffffff; /* Bright yellow for spinner */
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
user_input = st.text_input("Enter your prompt here:", "A portrait photo of Simbolo with graduation suit.")

if st.button("Generate"):
    with st.spinner("Generating image..."):
        response = query({"inputs": user_input})
        if response is not None and response.status_code == 200:
            try:
                image_bytes = response.content
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption=user_input)
            except Exception as e:
                st.error(f"Error processing image: {e}")
        elif response is None:
            st.error("Failed to get a response from the API.")

# Footer
st.markdown("<div class='footer'>Developed with ❤️ by Team Zee Kwat</div>", unsafe_allow_html=True)
