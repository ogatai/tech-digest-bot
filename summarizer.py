from ollama import chat


def summarize_japanese(text):
    if not text:
        return ""

    prompt = f"""
以下の記事を日本語で3行程度に要約してください。

{text[:2000]}
"""

    try:
        response = chat(
            model="qwen3:1.7b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        print("要約失敗:", e)
        return ""