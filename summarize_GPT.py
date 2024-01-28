def summarize_GPT(text, openai_api_key):
    from openai import OpenAI
    client = OpenAI(api_key=openai_api_key)

    try:
        response = client.completions.create(
            model="davinci-002",  # GPT model
            prompt=f"Please provide a concise 4 lines summary of the following text, giving a sense of the whole story:\n\n{text}",
            max_tokens=2000  # Adjust as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return str(e)
