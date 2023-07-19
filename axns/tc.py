import openai
import asyncio
from concurrent.futures import ThreadPoolExecutor

API_KEY = "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"

openai.api_key = API_KEY
memory = []


def janitor(obj=memory):
    if len(obj) > 7: obj.pop(0)


def text(query, inst="Follow all instructions."):
    loop = asyncio.get_event_loop()
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
