✅ Task Summary Report: Health Chatbot Model (CB_Model.py)
✅ Task Objective
To build and deploy a health-focused chatbot that uses a causal language model to generate human-like responses based on user queries. The chatbot loads a pretrained model and tokenizer and generates answers using natural language understanding.

📂 Dataset / Model Used
Type: Pretrained causal language model (compatible with Hugging Face transformers)

Format:

Model files stored in a local directory: CB_Model_model/

Tokenizer stored as: CB_Model_tokenizer.joblib

Library: transformers, torch, joblib

⚙️ Functionality Overview
Model Loading:

Loads model from a local directory using AutoModelForCausalLM

Loads tokenizer using joblib

Response Generation:

Accepts a user prompt (health-related question)

Constructs an input sequence: Question: ... Answer:

Generates a response using model.generate(...)

Class: HealthChatbot

get_response(prompt) returns a full-text answer.

🧪 Key Implementation Features
Robust error handling for missing files or loading issues

Uses GPU acceleration if available (device_map="auto")

Model limited to 300 tokens per response for control

Designed for conversational, health-related Q&A use cases
