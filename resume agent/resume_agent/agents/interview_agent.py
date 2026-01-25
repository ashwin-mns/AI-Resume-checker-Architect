import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_interview_questions(role, skills):
    prompt = f"""
You are Agent 4: Interview Question Generator.

Role: {role}

Candidate Skills:
{skills}

Generate:
1. 5 Technical Interview Questions
2. 3 HR Questions
3. 2 Project-Based Questions

Return as numbered list.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
