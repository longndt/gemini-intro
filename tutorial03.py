from utils import get_key
from google import genai

# Example of using system prompt.
# AI refers to the system prompt to generate the response
# AI has no memory, so it will not remember the context of the conversation
client = genai.Client(api_key=get_key())
system_prompt="You are a cat. You will answer questions as a cat. Convert words to meow, meoow, meooww, etc. based on the length of the word. ONLY MEOWS ALLOWED."

# Create a config with system_instruction to use when model is generating content
config = genai.types.GenerateContentConfig(system_instruction=system_prompt)
while True:
    question = input('[User]: ')
    if question == 'exit' or question == 'quit':
        break
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=[question],
        config=config   # config with system_instruction
    )
    print('[GenAI]:', response.text)