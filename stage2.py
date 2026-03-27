import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize the Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))                 

# Prompt user for input
user_input = input("Enter a message: ")

# Send user's message to the Chat Completions API
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {   # system sets behavior (personality, tone, restrictions)
            "role": "system",
            "content":  "You are a helpful assistant..."
        },
        {
            "role": "user",
            # actual user input
            "content": user_input
        }
    ]
)

# Extract assistant response text
assistant_reply = response.choices[0].message.content

# Output conversation
print(f"You: {user_input}")
# Print Assistant Response
print("Assistant:", response.choices[0].message.content)

# Retrieve token usage information
prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens

# Pricing for gpt-4o-mini (per 1,000,000 tokens)
input_price_per_million = 0.15
output_price_per_million = 0.60

# Calculate input and output costs
input_cost = (prompt_tokens / 1_000_000) * input_price_per_million
output_cost = (completion_tokens / 1_000_000) * output_price_per_million

# Calculate total cost
total_cost = input_cost + output_cost

# Display total cost formatted to 8 decimal places
print(f"Cost: ${total_cost:.8f}")
