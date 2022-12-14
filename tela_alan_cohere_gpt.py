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

title = st.text_area('Ask your question!')

if st.checkbox('Limit of answers:'):
    st.text_input('Type the number of answers you want:')

st.button('Send it to Alan and Google')

st.write('Select the answer framework to see its answers:')

col1, col2 = st.columns(2)

with col1:
    if st.checkbox("Alan"):
        st.text_area('Answers of Alan')
        st.checkbox('Save Alan answers to file')

st.checkbox('Save all to log')

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
    temperature_gpt_3 = st.slider('Temperature - GPT-3', min_value = 0.0, max_value = 1.0, step = 0.01)
    st.button('Run GPT-3!')
    st.checkbox('Save to file')

    st.markdown("""### Citation and explanation area of GPT-3""")

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Citation GPT-3'):
            st.text_area('GPT-3 citation')
            st.checkbox('Save this GPT-3 citation to file')

    with col2:
        if st.button('Explanation GPT-3'):
            st.text_area('GPT-3 explanation')
            st.checkbox('Save this GPT-3 explanation to file')
    

if st.checkbox("Cohere"):
    st.selectbox(
    'Select the answer framework to work with Cohere:',
     ['Alan', 'Google'])
    st.text_area('Free prompt to summarize with Cohere')
    temperature_cohere = st.slider('Temperature - Cohere', min_value = 0.0, max_value = 1.0, step = 0.01)
    st.button('Run Cohere!')
    st.checkbox('Save it to file')

    st.markdown("""### Citation and explanation area of Cohere""")

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Citation Cohere'):
            st.text_area('Cohere citation')
            st.checkbox('Save this Cohere citation to file')

    with col2:
        if st.button('Explanation Cohere'):
            st.text_area('Cohere explanation')
            st.checkbox('Save this Cohere explanation to file')

st.button('Click here to open comparisons and rankings between GPT-3 and Cohere responses')