import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define termination function
tools = [
    {
        "type": "function",
        "function": {
            "name": "end_conversation",
            "description": "Ends the conversation when the user wants to stop chatting.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]

# Initialize conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant for a simple CLI chat."}
]

# Pricing (same as Stage 2)
input_price_per_million = 0.15
output_price_per_million = 0.60

while True:
    user_input = input("Enter a message: ")

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools
    )

    message = response.choices[0].message

    # Check if assistant called termination function
    if message.tool_calls:
        tool_call = message.tool_calls[0]

        # Print function call ID
        print(tool_call.id)

        assistant_reply = None

        print(f"You: {user_input}")
        print(f"Assistant: {assistant_reply}")

        # Calculate cost
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens

        input_cost = (prompt_tokens / 1_000_000) * input_price_per_million
        output_cost = (completion_tokens / 1_000_000) * output_price_per_million
        total_cost = input_cost + output_cost

        print(f"Cost: ${total_cost:.8f}")

        break

    # Normal assistant response
    assistant_reply = message.content

    messages.append({"role": "assistant", "content": assistant_reply})

    print(f"You: {user_input}")
    print(f"Assistant: {assistant_reply}")

    # Calculate cost
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens

    input_cost = (prompt_tokens / 1_000_000) * input_price_per_million
    output_cost = (completion_tokens / 1_000_000) * output_price_per_million
    total_cost = input_cost + output_cost

    print(f"Cost: ${total_cost:.8f}")

