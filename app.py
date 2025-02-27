import openai

openai.api_key = "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"

try:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Hello, world!",
        max_tokens=5
    )
    print(response)
except openai.error.AuthenticationError as e:
    print("Authentication error:", e)
