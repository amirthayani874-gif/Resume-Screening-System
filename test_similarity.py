from resume_parser import extract_text_from_pdf
from similarity import calculate_similarity

resume_text = extract_text_from_pdf("uploads/resume.pdf")


with open("job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()


score = calculate_similarity(resume_text, job_description)


print(f"Resume-Job Similarity Score: {score:.2f}%")