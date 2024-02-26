import openai
import vectorstore

# Set up OpenAI API
openai.api_key = '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'

# Define your prompt
prompt = "Write a short story about a detective solving a mysterious crime."

# Connect to OpenAI API and generate text
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=150
)
generated_text = response.choices[0].text.strip()

# Connect to VectorStore
vs = vectorstore.VectorStore()

# Store the generated text and its vector embeddings in VectorStore
vs.set(generated_text, vectorstore.Vector(embeddings=response.choices[0].embedding))

# Retrieve embeddings from VectorStore
retrieved_embeddings = vs.get(generated_text).embeddings

# Print the generated text and retrieved embeddings
print("Generated Text:", generated_text)
print("Retrieved Embeddings:", retrieved_embeddings)
