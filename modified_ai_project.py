import tkinter as tk                   
import nltk                            
nltk.download('punkt')                 
from textblob import TextBlob          
from newspaper import Article       
import math   

def summerize():
    url = utext.get('1.0',"end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    pubdate.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    percent.config(state='normal')
    original_word_count.config(state='normal')
    summarized_word_count.config(state='normal')

    title.delete('1.0',"end")
    title.insert('1.0',article.title)

    pubdate.delete('1.0', "end")
    pubdate.insert('1.0', article.publish_date)

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    original_text = article.text
    original_word_count.delete('1.0', 'end')
    original_word_count.insert('1.0', f'{len(original_text.split())} words')

    analysis = TextBlob(original_text)
    sentiment.delete('1.0', "end")
    sentiment.insert("1.0",f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    ratio = len(summary.get('1.0', 'end-1c')) / len(original_text)
    percent.delete('1.0', "end")
    percent.insert('1.0', f'{round(ratio*100, 2)}% of the original text')

    summarized_word_count.delete('1.0', 'end')
    summarized_word_count.insert('1.0', f'{len(summary.get("1.0", "end-1c").split())} words')

    title.config(state='disabled')
    pubdate.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    percent.config(state='disabled')
    original_word_count.config(state='disabled')
    summarized_word_count.config(state='disabled')

    polarity = analysis.polarity
    angle = polarity * 90
    x = 50 + 40 * math.sin(math.radians(angle))
    y = 50 - 40 * math.cos(math.radians(angle))
    arrow_canvas.delete("arrow")
    color = "black"
    if polarity > 0:
        color = "green"
    elif polarity < 0:
        color = "red"
    arrow_canvas.create_line(50, 50, x, y, width=5, arrow="last", fill=color, tags="arrow")
                             
root = tk.Tk()
root.title("News Summarizer ")
root.geometry('1200x600')

tlable = tk.Label(root, text="Title")
tlable.pack()    

# Create the arrow canvas
arrow_canvas = tk.Canvas(root, width=100, height=100)
arrow_canvas.pack()

# Create the semicircle
arrow_canvas.create_arc(10, 10, 90, 90, start=0, extent=180, style="arc")

# Create the tick marks
for i in range(-10, 11, 2):
    angle = i * 9
    x1 = 50 + 35 * math.sin(math.radians(angle))
    y1 = 50 - 35 * math.cos(math.radians(angle))
    x2 = 50 + 40 * math.sin(math.radians(angle))
    y2 = 50 - 40 * math.cos(math.radians(angle))
    arrow_canvas.create_line(x1, y1, x2, y2)

# Create the arrow line
arrow_canvas.create_line(50, 50, 50, 10, width=5)

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg ='white')
title.pack()


plable = tk.Label(root, text="Publication Date")
plable.pack()

pubdate = tk.Text(root, height=1, width=140)
pubdate.config(state='disabled', bg ='white')
pubdate.pack()

slable = tk.Label(root, text="Summary")
slable.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg ='white')
summary.pack()

selable = tk.Label(root, text="Sentiment analysis")
selable.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg ='white')
sentiment.pack()

selable = tk.Label(root, text="percent")
selable.pack()

percent = tk.Text(root, height=1, width=140)
percent.config(state='disabled', bg ='white')
percent.pack()

selable = tk.Label(root, text="original_word_count")
selable.pack()

original_word_count = tk.Text(root, height=1, width=140)
original_word_count.config(state='disabled', bg ='white')
original_word_count.pack()

selable = tk.Label(root, text="summarized_word_count")
selable.pack()

summarized_word_count = tk.Text(root, height=1, width=140)
summarized_word_count.config(state='disabled', bg ='white')
summarized_word_count.pack()

ulable = tk.Label(root, text="URL")
ulable.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize" , command=summerize)
btn.pack()

root.mainloop()
