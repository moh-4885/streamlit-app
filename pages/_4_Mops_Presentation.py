import streamlit as st
import reveal_slides as rs
import os

#### change the style file 
st.set_page_config(
    page_title="mlps presentation ",
    initial_sidebar_state='expanded',
    layout='wide'
)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def load_slides(slide_directory):
  slides = []
  for filename in os.listdir(slide_directory):
    if filename.endswith(".html"):
      with open(os.path.join(slide_directory, filename), "r") as f:
        content = f.read()
        slides.append(content)
  return slides

# Example usage
slides = load_slides("./pages/html_slides")  # Replace with your slide directory path

st.title("MLOps Frameworks Presentation")  # Add a title to your Streamlit app

# Iterate through slides and display them using reveal_slide
for slide in slides:
  rs.slides(slide)
  