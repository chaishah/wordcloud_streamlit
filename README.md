
# PDF Word Cloud Generator

This is a Streamlit app that generates a word cloud from a PDF file.

## Requirements

- Python 3.6+
- Streamlit
- PyPDF2
- wordcloud
- PIL (Python Imaging Library)
- Matplotlib

You can install the required Python packages using pip:



## Usage

To run the app, navigate to the directory containing `app.py` and run the following command:


This will start the app and open it in your default browser. You can then upload a PDF file to generate a word cloud.

## How it works

The app first prompts you to upload a PDF file. Once you select a file, the app extracts the text from the PDF file using PyPDF2. It then generates a word cloud from the extracted text using the wordcloud package.

The resulting word cloud is displayed in the app using Matplotlib, and the user can download the image or copy it to the clipboard.

## Acknowledgements

This app was created using Streamlit, PyPDF2, wordcloud, PIL (Python Imaging Library), and Matplotlib.


![Word cloud example](/Sample.png)


...


### Chaitya Shah