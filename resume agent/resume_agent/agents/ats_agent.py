from roles import JOB_ROLES

def ats_matcher(resume_text, role):
    required_skills = JOB_ROLES.get(role, [])
    text = resume_text.lower()

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in text:
            matched.append(skill)
        else:
            missing.append(skill)

    # Avoid division by zero
    if not required_skills:
        score = 0
    else:
        score = int((len(matched) / len(required_skills)) * 100)

    return {
        "ats_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }
