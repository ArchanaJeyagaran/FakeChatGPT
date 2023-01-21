from transformers import pipeline, set_seed
generator = pipeline('text-generation', model = 'gpt2')
set_seed(42)
x = generator("Hello, I am a girl who wants to be a data scientist,", max_length=60, num_return_sequences = 1) 
print(x)
