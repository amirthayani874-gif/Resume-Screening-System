from resume_info import SKILLS, SKILL_ALIASES


def extract_job_skills(job_description):
    job_description = job_description.lower()

    required_skills = set()

    for skill in SKILLS:
        if skill in job_description:
            required_skills.add(skill)

    for alias, standard_skill in SKILL_ALIASES.items():
        if alias in job_description:
            required_skills.add(standard_skill)

    return list(required_skills)


def compare_skills(resume_skills, required_skills):
    resume_skills = set(resume_skills)
    required_skills = set(required_skills)

    matched_skills = resume_skills.intersection(required_skills)
    missing_skills = required_skills - resume_skills

    if required_skills:
        skill_score = (len(matched_skills) / len(required_skills)) * 100
    else:
        skill_score = 0

    return matched_skills, missing_skills, skill_score


def calculate_final_score(skill_score, similarity_score):
    final_score = (
        (skill_score * 0.70) +
        (similarity_score * 0.30)
    )

    return final_score