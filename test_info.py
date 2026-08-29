from resume_parser import extract_text_from_pdf
from resume_info import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    extract_education,
    extract_experience,
    format_education,
    format_experience
)

pdf_path = "uploads/resume.pdf"

text = extract_text_from_pdf(pdf_path)

name = extract_name(text)
email = extract_email(text)
phone = extract_phone(text)
skills = extract_skills(text)
education = extract_education(text)
experience = extract_experience(text)
formatted_education = format_education(education)
formatted_experience = format_experience(experience)

print("Name:", name)
print("Email:", email)
print("Phone:", phone)

print("\nSkills Found:")

for skill in skills:
    print("-", skill)


print("\nEducation:")

for i, entry in enumerate(formatted_education, start=1):
    print(f"\n{i}.")
    for line in entry if isinstance(entry, list) else [entry]:
        print("  ", line)


print("\nExperience:")

for line in formatted_experience:
    print("-", line)