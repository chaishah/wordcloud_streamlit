import streamlit as st
from PyPDF2 import PdfReader
import io
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import plotly.graph_objects as go

def pdf_to_text(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()
        if page_text is None:
            print(f"Error: Could not extract text from page {page_num + 1}")
        else:
            text += page_text
    return text

import plotly.graph_objects as go
from wordcloud import STOPWORDS
from wordcloud import WordCloud

def generate_wordcloud(text):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000, width=800, height=600)
    wordcloud.generate(text)
    word_frequencies = wordcloud.process_text(text)

    fig = go.Figure(data=[go.Scatter(
        x=[0.5],
        y=[0.5],
        text=list(word_frequencies.keys()),
        mode='text',
        textfont=dict(size=[v*10 for v in word_frequencies.values()], color='#000000'),
    )])
    fig.update_layout(
        title_text='Word Cloud',
        xaxis=dict(showticklabels=False),
        yaxis=dict(showticklabels=False),
        width=800,
        height=600
    )
    return fig




st.title("PDF Word Cloud Generator")
st.write("Upload a PDF file to generate a word cloud.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Extracting text and generating word cloud..."):
        pdf_file = io.BytesIO(uploaded_file.read())
        pdf_text = pdf_to_text(pdf_file)
        wordcloud_fig = generate_wordcloud(pdf_text)

    st.plotly_chart(wordcloud_fig)
else:
    st.info("Please upload a PDF file to generate a word cloud.")
