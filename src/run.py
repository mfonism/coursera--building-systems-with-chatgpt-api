import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=0
    )
    return response.choices[0].message.content


def get_completion_from_messages(
    messages, model="gpt-4o-mini", temperature=0, max_tokens=500
):
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=temperature, max_tokens=max_tokens
    )
    return response.choices[0].message.content


messages_01 = [
    {
        "role": "system",
        "content": "You are an assistant who responds in the style of Dr Seuss.",
    },
    {"role": "user", "content": "write me a very short poem about a happy carrot"},
]

messages_02 = [
    {"role": "system", "content": "All your responses must be one sentence long."},
    {"role": "user", "content": "write me a story about a happy carrot"},
]


def get_completion_and_token_count(
    messages, model="gpt-4o-mini", temperature=0, max_tokens=500
):
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=temperature, max_tokens=max_tokens
    )

    content = response.choices[0].message.content
    token_dict = {
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
    }

    return content, token_dict


messages_03 = [
    {
        "role": "system",
        "content": "You are an assistant who responds in the style of Dr Seuss.",
    },
    {"role": "user", "content": "write me a very short poem about a happy carrot"},
]

breakpoint()
