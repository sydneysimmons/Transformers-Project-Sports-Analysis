import gradio as gr
from transformers import pipeline
from newspaper import Article

summarizer_fb_bart = pipeline("summarization", model = "facebook/bart-large-cnn")

def summarizer(url):
  def article_to_text(url):
    url = url

    # download and parse article
    article = Article(url)
    article.download()
    article.parse()
    
    # print article text
    text = article.text

    # account for article length and cut it off
    words = text.split()
    if len(words) > 512:
      words = words[:512]
    text = ' '.join(words)

    return text

  return summarizer_fb_bart(article_to_text(url))

iface = gr.Interface(fn=summarizer, inputs=gr.Textbox(lines=2, label="Input URL to Sports Article Here:"), outputs="text", title = "Sports Article Summarization")
iface.launch()

