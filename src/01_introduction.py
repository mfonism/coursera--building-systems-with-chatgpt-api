from util import get_completion, get_completion_and_token_count

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


messages_03 = [
    {
        "role": "system",
        "content": "You are an assistant who responds in the style of Dr Seuss.",
    },
    {"role": "user", "content": "write me a very short poem about a happy carrot"},
]

breakpoint()
