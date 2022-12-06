import gradio as gr
from transformers import pipeline
from newspaper import Article

question_answerer = pipeline("question-answering")
summarizer_fb_bart = pipeline("summarization", model = "facebook/bart-large-cnn")

def question_answer(url, question):
    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    result = question_answerer(question=question, context=text)
    answer = result['answer']
    return answer

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
  summary = summarizer_fb_bart(article_to_text(url))
  return summary[0]['summary_text']

with gr.Blocks() as demo:
    url = gr.Textbox(label="Input URL to Sports Article Here:")
    question = gr.Textbox(label="Type your question here:")
    answer_btn = gr.Button("Ask Question")
    output = gr.Textbox(label="Answer")
    answer_btn.click(fn=question_answer, inputs=[url,question], outputs=output)
    summary_btn = gr.Button("Summarize")
    summary = gr.Textbox(label="Sports Article Summarization")
    summary_btn.click(fn=summarizer, inputs=url, outputs=summary)

demo.launch()