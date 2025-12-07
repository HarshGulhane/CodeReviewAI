import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_code_with_llm(code: str) -> str:
    prompt = f"""
    Review the following source code for:
    - readability
    - modularity
    - coding best practices
    - maintainability
    - possible bugs

    Provide a clear structured report.

    CODE:
    {code}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # ✅ FIX: Groq returns message as an object, so use .content
    return response.choices[0].message.content
