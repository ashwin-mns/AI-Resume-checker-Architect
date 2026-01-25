import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text, role, missing_skills, breakdown):
    prompt = f"""
You are an AI Resume Optimization Agent.

Target Role: {role}

Resume Breakdown Scores:
- Skills Score: {breakdown['skills_score']}
- Projects Score: {breakdown['project_score']}
- Experience Score: {breakdown['experience_score']}
- Education Score: {breakdown['education_score']}
- Overall Score: {breakdown['overall_score']}

Missing Skills: {missing_skills}

TASK:
1. Give role-specific improvements.
2. Suggest how to improve weakest section.
3. Rewrite Professional Summary for {role}.
4. Suggest 2 resume-worthy projects for this role.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
