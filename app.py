from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Streamlit app with custom favicon
st.set_page_config(page_title="ECO-SHOP", layout="wide", page_icon="assets/favicon.ico")

# Function to load Gemini model and get responses
def get_gemini_response(image, user_input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Define the input prompt
    input_prompt = f"""add emojies if you want
Analyze the product image and extract the following details. Use the additional user input for context or specific instructions if provided.
 
Product description:

- **Category:** **[Product category]**
- **Name:** **[Name of the product]**
- **Size:** **[Size or quantity]**
- **Additional Details:** **[Other relevant details]**

Nutritional Information:

- **Protein:** **[value]**
- **Sugars:** **[value]**
- **Fat:** **[value]**
- **Fiber:** **[value]**
- **Sodium:** **[value]**
- **Caffeine:** **[value]**
- **Other Nutrients:** **[value]**

Warnings:

- **[Nutrient]**: **[Description of health risk or potential issues related to this nutrient which excess can cause health issues]**

Environmental Impact:

- **Carbon Footprint:** **[Description]**
- **Water Usage:** **[Description]**
- **Recyclability:** **[Description]**
- **Packaging Waste:** **[Description]**

Healthier & More Eco-Friendly Alternatives:

- **Alternative 1:** **[Suggest eco-conscious alternatives]**
- **Alternative 2:** **[Recommend innovative and sustainable ideas]**
- **Alternative 3:** **[Highlight eco-shop alternatives]**
- **Alternative 4:** **[Sustainable product suggestions]**

DIY Ideas Using Packaging or Waste:

- **DIY Idea 1:** **[Reuse packaging]**
- **DIY Idea 2:** **[Sustainable crafting]**
- **DIY Idea 3:** **[Eco-friendly projects]**


User Input:
{user_input}

If any information is unavailable, return "None" for that field. Ensure concise and formatted output, and bold the following sections: Category, Name, Size, Additional Details, Sugars, Protein, Fat, Fiber, Sodium, Caffeine, Other Nutrients, Carbon Footprint, Water Usage, Recyclability, Packaging Waste, Healthier & More Eco-Friendly Alternatives, DIY Ideas Using Packaging or Waste.
"""
    
    # Get response from the model
    response = model.generate_content([input_prompt, image])
    return response.text

# Display header first
st.markdown(
    """
    <div style="background-color:#228B22; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">🌿 Welcome to ECO-SHOP 🌿</h1>
        <h3 style="color:white; text-align:center;">Empowering Sustainable Living through AI Analysis</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display image below the header
st.image(r"C:\Users\DELL\Desktop\chatbot\assets\image.jpg", use_container_width=True)

# File uploader and text input for analysis
st.markdown("### 📤 Upload an Image:")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

st.markdown("### ✍️ Provide Additional Context:")
user_input = st.text_input("Enter any specific instructions or context:")

# Display uploaded image
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Image", use_container_width=True)

# Button to process the image and text input
submit = st.button("🌟 Analyze with Sustainify")

# Function to display the analysis result
def display_analysis_result(response):
    st.markdown(
        f"""
        <div class="analysis-result">
            <pre>{response}</pre>
        </div>
        """,
        unsafe_allow_html=True,
    )

# If the submit button is clicked
if submit:
    if not image:
        st.warning("⚠️ Please upload an image.")
    else:
        response = get_gemini_response(image, user_input)

        # Display the result
        st.markdown(
            """
            <div style="background-color:#FFD700; padding:10px; border-radius:10px;">
                <h2 style="color:black; text-align:center;">🔍 Analysis Result:</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

        display_analysis_result(response)

        # "Happy and Healthy Shopping" quote section
        st.markdown(
            """
            <div style="background-color:#90EE90; padding:10px; border-radius:10px; margin-top:20px;">
                <h2 style="color:black; text-align:center; font-weight:bold;">🌱Shop Green, Shop Smart, Shop with  Eco-Shop 🌱</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
