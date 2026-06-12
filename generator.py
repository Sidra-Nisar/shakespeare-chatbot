from transformers import pipeline
from transformers import set_seed
set_seed(42)


generator = pipeline("text-generation", model="distilgpt2")

def generate_response(user_input, quotes=[]):
    prompt = " ".join(quotes) + "\n" + user_input
    if len(prompt) > 300:
       prompt = prompt[-300:]
    result = generator(
    prompt,
    max_length=50,
    num_return_sequences=1,
    truncation=True,
    temperature=0.7,
    top_k=50,
    repetition_penalty=1.2
)
    return result[0]["generated_text"]
