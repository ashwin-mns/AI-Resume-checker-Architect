import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_resume(resume_text, role):
    prompt = f"""
You are an AI Resume Writer.

Rewrite this resume professionally for the role of {role}.
Output should contain:

1. Professional Summary
2. Skills Section (ATS optimized)
3. Projects Section (improved)
4. Experience Section (if missing, suggest)
5. Education Section

Resume Content:
{resume_text}

Return ONLY the improved resume text in clean format.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
