from roles import JOB_ROLES

def ats_match_score(resume_text, role):
    required_skills = JOB_ROLES.get(role, [])

    resume_text_lower = resume_text.lower()

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in resume_text_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    # Avoid division by zero if no skills are required
    if not required_skills:
        score = 0
    else:
        score = int((len(matched) / len(required_skills)) * 100)

    return {
        "role": role,
        "ats_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }
