import streamlit as st
from PIL import Image
from story_generator import generate_story_from_images

st.title("AI Story Generator from Image ")
st.markdown("Upload 1-10 images, choose a style and let AI write and narrate a story for you.")

with st.sidebar:
    st.header("Controls")

    uploaded_files = st.file_uploader("Upload your images",
                     type=['png','jpg','jpeg'],
                     accept_multiple_files=True)
    
    story_style = st.selectbox(
        "Choose a style for your story",
        ("comedy","Thriller","adventure","Fairy Tale","Sci-fi","Mystery","Morale")
    )

    generate_button = st.button("Generate Story & Narration", type = 'primary')



if generate_button:
    if not uploaded_files:
        st.warning("Please Upload a file first to generate the story")

    elif len(uploaded_files) > 10: 
        st.warning("Please Upload a maximum of 10 files")
    else:
        with st.spinner("AI is writing and narrating your story"):
            try:
                pil_image = [Image.open(uploaded_file) for uploaded_file in uploaded_files]
                st.subheader("Your Visual Inspiration: ")
                image_columns = st.columns(len(pil_image))
    
                for i, image in enumerate(pil_image):
                    with image_columns[i]:
                        st.image(image,use_container_width=True)

                generate_story = generate_story_from_images(pil_image,story_style)

                if "Error" in generate_story or "failed" in generate_story or "API Key" in generate_story:
                    st.error(generate_story)
                else:
                    st.subheader(f"Your {story_style} story: ")
                    st.success(generate_story)

            except Exception as e:
                st.error(f"An Application Error Occured: {e}")




