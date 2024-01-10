# Summarizer Chat Bot

Model used: facebook/bart-large-cnn 

Documentation: https://huggingface.co/facebook/bart-large-cnn

**Model description**
BART is a transformer encoder-encoder (seq2seq) model with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder. BART is pre-trained by (1) corrupting text with an arbitrary noising function, and (2) learning a model to reconstruct the original text.

BART is particularly effective when fine-tuned for text generation (e.g. summarization, translation) but also works well for comprehension tasks (e.g. text classification, question answering). This particular checkpoint has been fine-tuned on CNN Daily Mail, a large collection of text-summary pairs.

---
title: Summarizer Chatbot
emoji: 👁
colorFrom: blue
colorTo: blue
sdk: gradio
sdk_version: 4.13.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
