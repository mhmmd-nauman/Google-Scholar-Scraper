from pypdf import PdfReader

import glob 
import os 
import re
import sys

pdf_files = glob.glob(os.path.join("Big Data Education",'*.pdf'))

text = ""
for pdf_file in pdf_files:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text() + "\n"

#print(text)

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
comment_words = ''
stopwords = set(STOPWORDS)
tokens = text.split()
for i in range(len(tokens)):
    tokens[i] = tokens[i].lower()

comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800,
    background_color ='white',
    stopwords = stopwords,
    min_font_size = 10).generate(comment_words)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()