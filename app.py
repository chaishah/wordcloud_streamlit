import streamlit as st
from PyPDF2 import PdfReader
import io
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import matplotlib.pyplot as plt
def pdf_to_text(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

def generate_wordcloud(text):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000, width=800, height=600)
    wordcloud.generate(text)
    # Create a matplotlib figure and adjust the dpi value
    fig = plt.figure(figsize=(8, 6), dpi=300)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    # Convert the figure to an image
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    image = Image.open(buf)
    return image

st.title("PDF Word Cloud Generator")
st.write("Upload a PDF file to generate a word cloud.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Extracting text and generating word cloud..."):
        pdf_file = io.BytesIO(uploaded_file.read())
        pdf_text = pdf_to_text(pdf_file)
        wordcloud_image = generate_wordcloud(pdf_text)

    st.image(wordcloud_image, caption="Word Cloud")
else:
    st.info("Please upload a PDF file to generate a word cloud.")
