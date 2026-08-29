from resume_parser import extract_text_from_pdf
from resume_info import extract_skills
from job_matcher import (
    extract_job_skills,
    compare_skills,
    calculate_final_score
)
from similarity import calculate_similarity


resume_text = extract_text_from_pdf("uploads/resume.pdf")


resume_skills = extract_skills(resume_text)


with open("job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()


required_skills = extract_job_skills(job_description)


matched_skills, missing_skills, skill_score = compare_skills(
    resume_skills,
    required_skills
)


similarity_score = calculate_similarity(
    resume_text,
    job_description
)


final_score = calculate_final_score(
    skill_score,
    similarity_score
)


print("\n==============================")
print("     RESUME SCREENING RESULT")
print("==============================")

print("\nResume Skills:")

for skill in resume_skills:
    print("-", skill)


print("\nRequired Skills:")

for skill in required_skills:
    print("-", skill)


print("\nMatched Skills:")

for skill in matched_skills:
    print("✓", skill)


print("\nMissing Skills:")

for skill in missing_skills:
    print("✗", skill)


print(f"\nSkill Match Score: {skill_score:.2f}%")

print(f"Text Similarity Score: {similarity_score:.2f}%")

print(f"Final Match Score: {final_score:.2f}%")