from openai import OpenAI

try:
    from keys import OPENAI_KEY
except ImportError:
    OPENAI_KEY = None


def send_chatgpt_prompt(
    prompt_message, max_response_tokens=3000, model="gpt-4o"
):
    """
    Send a prompt to OpenAI's GPT model and return the response.

    Parameters
    ----------
    prompt_message : str
        The message to send to the model.
    max_response_tokens : int, optional
        The maximum number of tokens to generate, by default 3000.
    model : str, optional
        The OpenAI GPT model to use, by default "gpt-4o".

    Returns
    -------
    str
        The response message from the model.
    """
    msg = "Please enter your OpenAI API key: "
    openai_key = (
        OPENAI_KEY if OPENAI_KEY else input(msg)
    )

    client = OpenAI(api_key=openai_key)

    response = client.chat.completions.with_raw_response.create(
        messages=[
            {
                "role": "system",
                "content": "You are a Machine Learning Engineer.",
            },
            {"role": "user", "content": prompt_message},
        ],
        model=model,
        max_tokens=max_response_tokens,
    )

    completion = response.parse()
    response_message = completion.choices[0].message.content
    return response_message


if __name__ == "__main__":
    response_message = send_chatgpt_prompt(
        "Explain unit testing in Python. Tell all you know please",
        max_response_tokens=10,
    )
    print(response_message)
