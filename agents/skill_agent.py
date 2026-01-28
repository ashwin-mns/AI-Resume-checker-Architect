import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_skills(resume_text):
    prompt = f"""
You are Agent 1: Skill Extractor.

Extract the following from resume:
1. Technical Skills
2. Soft Skills
3. Key Projects
4. Education Details

Resume:
{resume_text}

Return output in JSON format.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
