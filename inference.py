from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

tokenizer = T5Tokenizer.from_pretrained("/app/model")
model = T5ForConditionalGeneration.from_pretrained("/app/model")

def predict(request):
    inputs = tokenizer(request.json['input'], return_tensors="pt", max_length=2048, padding="max_length", truncation=True)
    outputs = model.generate(**inputs, max_length=2048, num_return_sequences=1)  # Adjust the max_length value
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"output": decoded_output}

def health(request):
    return {"status": "UP"}

