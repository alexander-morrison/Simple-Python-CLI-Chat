import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize the Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create Chat Completion
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {   # system sets behavior (personality, tone, restrictions)
            "role": "system",
            "content":  "You are a helpful assistant..."
        },
        {
            # user message
            "role": "user",
            # actual user input
            "content": "What are you?"
        }
    ]
)

# Print User Line
print("You: What are you?")
# Print Assistant Response
print("Assistant:", response.choices[0].message.content)




                

