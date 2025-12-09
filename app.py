import streamlit as st


st.title("AI Story Generator from Image ")
st.markdown("Upload 1-10 images, choose a style and let AI write and narrate a story for you.")

with st.sidebar:
    st.header("Controls")

    uploaded_files = st.file_uploader("Upload your images",
                     type=['png','jpg','jpeg'],
                     accept_multiple_files=True)
    
    story_style = st.selectbox(
        "Choose a style for your story",
        ("comedy","thriller","adventure","Fairy Tale","Sci-fi","Mystery")
    )

    generate_button = st.button("Generate Story & Narration", type = 'primary')



if generate_button:
    if not uploaded_files:
        st.warning("Please Upload a file first to generate the story")

    elif len(uploaded_files) > 10: 
        st.warning("Please Upload a maximum of 10 files")
    else:
        with st.spinner("AI is writing and narrating your story"):
            st.write("hello")

    



