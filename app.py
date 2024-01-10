# -*- coding: utf-8 -*-
""" 
summarizer chat bot by sajadahmadia
"""

from transformers import pipeline, Conversation

import gradio as gr

summarizer = pipeline(task = "summarization", model="facebook/bart-large-cnn")

#creating the bot
def summarizer_bot(message, history):
    return summarizer(message, min_length=5, max_length=140)[0]['summary_text']

demo_summarizer = gr.ChatInterface(summarizer_bot, title="Summarizer Chatbot", description="Enter your text, and the chatbot will return the summarized version.\n(It might take a little time!)")

demo_summarizer.launch()