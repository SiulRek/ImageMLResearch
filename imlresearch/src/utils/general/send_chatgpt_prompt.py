try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

try:
    from keys import OPENAI_KEY
except ImportError:
    OPENAI_KEY = None


def _require_openai_dependency():
    if OpenAI is None:
        raise ImportError(
            "Optional dependency 'openai' is required for AI analysis. "
            "Install it with: pip install openai==1.34.0"
        )


def _get_openai_api_key(provided_key):
    if provided_key:
        return provided_key
    if OPENAI_KEY:
        return OPENAI_KEY
    return input("Please enter your OpenAI API key: ").strip()


def send_chatgpt_prompt(
    prompt_message,
    max_response_tokens=3000,
    model="gpt-4o",
    api_key=None,
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
    api_key : str | None, optional
        OpenAI API key. If not provided, the function tries OPENAI_KEY
        from keys.py and finally prompts the user.

    Returns
    -------
    str
        The response message from the model.
    """
    _require_openai_dependency()
    resolved_api_key = _get_openai_api_key(api_key)

    client = OpenAI(api_key=resolved_api_key)

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
    return completion.choices[0].message.content


if __name__ == "__main__":
    response_message = send_chatgpt_prompt(
        "Explain unit testing in Python. Tell all you know please",
        max_response_tokens=10,
    )
    print(response_message)