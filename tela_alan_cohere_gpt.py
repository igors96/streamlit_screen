import streamlit as st
from PIL import Image

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #0E0C25;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html = True)

image = Image.open('logo-dark-removebg-preview.png')

st.image(image)

st.title('Alan Post-Processing Layer')

st.markdown("""

This app performs comparisons between the responses between Alan and Google, using Cohere and GPT-3.

""")

title = st.text_area('Ask your question')

col1, col2 = st.columns(2)

with col1:
    if st.checkbox('Limit of answers'):
        st.text_input('Type the number of answers you want')

with col2:
    st.checkbox('Save all to log')

col1, col2 = st.columns(2)

with col1:
    if st.checkbox("Alan"):
        st.text_area('Answers of Alan')
        st.checkbox('Save Alan answers to file')

st.button('Click here to open comparisons and rankings between Alan and Google answers')

with col2:
    if st.checkbox("Google"):
        st.text_area('Answers of Google')
        st.checkbox('Save Google answers to file')

st.markdown("""### Prompt Engineering""")

if st.checkbox("GPT-3"):
    st.selectbox(
    'Select the answer framework to work with GPT-3:',
     ['Alan', 'Google'])
    st.text_area('Free prompt to summarize with GPT-3')
    st.checkbox('Save to file')

    st.markdown("""### Summarization and explanation area of GPT-3""")

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Summary'):
            st.text_area('GPT-3 summarization')
            st.checkbox('Save this GPT-3 summary to file')

    with col2:
        if st.button('Explanation'):
            st.text_area('GPT-3 explanation')
            st.checkbox('Save this GPT-3 explanation to file')
    

if st.checkbox("Cohere"):
    st.selectbox(
    'Select the answer framework to work with Cohere:',
     ['Alan', 'Google'])
    st.text_area('Free prompt to summarize with Cohere')
    st.checkbox('Save to file')

    st.markdown("""### Summarization and explanation area of Cohere""")

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Summary'):
            st.text_area('Cohere summarization')
            st.checkbox('Save this Cohere summary to file')

    with col2:
        if st.button('Explanation'):
            st.text_area('Cohere explanation')
            st.checkbox('Save this Cohere explanation to file')

st.button('Click here to open comparisons and rankings between GPT-3 and Cohere responses')