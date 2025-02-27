import openai

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual OpenAI API key

# Function to get AI response using the old API (Completion)
def get_ai_response(prompt):
    try:
        # Correct API call using the old method for completions
        response = openai.Completion.create(
            model="text-davinci-003",  # You can use other models like "gpt-3.5-turbo"
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"
