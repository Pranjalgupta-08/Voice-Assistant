from openai import OpenAI
import time
import openai
# from openai.error import RateLimitError

client=OpenAI(
    api_key="sk-_M0vVIugVL0ChrZwQelNQOpJDxHPZqFKJiV-qqKjJ2T3BlbkFJSlo_8tXDelzNPU_1bkZh6yss3ZmiElSkM8K4OrzKAA",
)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant named jarvis like alexa and google cloud."},
        {
            "role": "user",
            "content": "What is programming."
        }
    ]
)

print(completion.choices[0].message)