import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_code(code, language, mode):
    if mode == "Beginner":
        instruction = "Explain in very simple terms for a beginner with examples."
    else:
        instruction = "Explain technically with proper depth and terminology."

    prompt = f"""
You are a senior software engineer and teacher.

Task:
Explain the following {language} code.

Mode: {mode}
Instruction: {instruction}

Also include:
- Step-by-step explanation
- Purpose of code
- If any bugs or improvements exist, mention them

Code:
{code}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content