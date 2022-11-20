import streamlit as st

st.title('Alan Post-Processing Layer')

st.markdown("""

This app performs comparisons between the responses between Alan and Google, using Cohere and GPT-3

""")

title = st.text_area('Ask your question')

col1, col2 = st.columns(2)

with col1:
    limit_answers = st.checkbox('Limit of answers')
    if limit_answers:
        number_answers = st.text_input('Type the number of answers you want')

with col2:
    save_all_to_log = st.checkbox('Save all to log')

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

if st.checkbox("Cohere"):
    st.selectbox(
    'Select the answer framework to work with Cohere:',
     ['Alan', 'Google'])
    st.text_area('Free prompt to summarize with Cohere')
    st.checkbox('Save it to file')

st.markdown("""### Summarization area""")
st.text_area('GPT-3 summary')
st.checkbox('Save this GPT-3 summary to file')
st.text_area('Cohere summary')
st.checkbox('Save this Cohere summary to file')

st.button('Click here to open comparisons and rankings between GPT-3 and Cohere responses')
# if st.checkbox('Show dataframe'):