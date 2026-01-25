import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def resume_writer(resume_text, role, missing_skills):
    prompt = f"""
You are Agent 3: Resume Writer.

Rewrite the resume professionally for the role: {role}

Missing ATS Keywords to include:
{missing_skills}

Improve:
- Summary
- Skills section
- Projects descriptions

Return clean formatted resume text.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
