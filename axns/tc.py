import openai
from concurrent.futures import ThreadPoolExecutor

API_KEY = "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"

openai.api_key = API_KEY
memory = []


def janitor(obj=memory):
    if len(obj) > 7: obj.pop(0)

def text(query, inst="Follow all instructions."):
    if query: memory.append("User: " + query)
    janitor(memory)

    textQuery = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": inst},
            {"role": "user", "content": query}
        ],
    )

    textQuery = textQuery["choices"][0]["message"]["content"]

    memory.append("You: " + textQuery)
    janitor(memory)

    return textQuery
