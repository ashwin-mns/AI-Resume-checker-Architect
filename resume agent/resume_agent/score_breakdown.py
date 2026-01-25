def resume_score_breakdown(resume_text, missing_skills):
    text = resume_text.lower()

    # Section presence checks
    has_skills = "skills" in text
    has_projects = "project" in text
    has_experience = "experience" in text or "internship" in text
    has_education = "education" in text or "b.e" in text or "bachelor" in text

    # Base scoring weights
    skills_score = 70 if has_skills else 30
    project_score = 80 if has_projects else 40
    experience_score = 75 if has_experience else 25
    education_score = 90 if has_education else 50

    # Reduce skills score if many missing keywords
    penalty = len(missing_skills) * 3
    skills_score = max(0, skills_score - penalty)

    # Final ATS score (average)
    overall = int((skills_score + project_score + experience_score + education_score) / 4)

    return {
        "overall_score": overall,
        "skills_score": skills_score,
        "project_score": project_score,
        "experience_score": experience_score,
        "education_score": education_score
    }
