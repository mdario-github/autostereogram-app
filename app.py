# File for the streamlit app.

import streamlit as st
from src.depthmap import image_to_depthmap
from src.stereogram import generate_autostereogram
from PIL import Image
import io

# --- Streamlit page configuration ---
st.set_page_config(
    page_title="Autostereogram Generator",
    layout="wide"
)

# --- App title and description ---
st.title("🎨 Autostereogram Generator")
st.write(
    "Upload an image and transform it into a 3D autostereogram! "
    "Use the depth estimation model MiDaS and a stereogram algorithm."
)

# --- File uploader ---
uploaded_file = st.file_uploader(
    "Choose an image file",
    type=["jpg", "jpeg", "png"]
)

# --- Main workflow ---
if uploaded_file:
    # Display original image
    st.image(uploaded_file, caption="Original image", use_column_width=True)

    # Button to trigger processing
    if st.button("🔮 Generate autostereogram"):
        # Step 1: Generate depth map
        with st.spinner("Generating depth map with MiDaS..."):
            depth_img = image_to_depthmap(uploaded_file, model_type="DPT_Hybrid")

        st.image(depth_img, caption="Generated depth map", use_column_width=True)

        # Step 2: Generate stereogram
        with st.spinner("Generating autostereogram..."):
            stereogram = generate_autostereogram(depth_img, eye_separation=15)

        st.image(stereogram, caption="Autostereogram", use_column_width=True)

        # Step 3: Download button
        buf = io.BytesIO()
        stereogram.save(buf, format="PNG")
        st.download_button(
            label="📥 Download autostereogram",
            data=buf.getvalue(),
            file_name="stereogram.png",
            mime="image/png"
        )
