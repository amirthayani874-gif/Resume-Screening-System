from flask import Flask, render_template, request, send_file, session
import os

from report_generator import generate_report

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

from job_matcher import (
    extract_job_skills,
    compare_skills,
    calculate_final_score
)

from similarity import calculate_similarity


app = Flask(__name__)

app.secret_key = "resume_screening_secret_key"

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]

    job_description = request.form["job_description"]

    resume_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(resume_path)

    resume_text = extract_text_from_pdf(resume_path)

    name = extract_name(resume_text)

    email = extract_email(resume_text)

    phone = extract_phone(resume_text)

    resume_skills = extract_skills(resume_text)

    education = extract_education(resume_text)

    experience = extract_experience(resume_text)

    formatted_education = format_education(education)

    formatted_experience = format_experience(experience)

    required_skills = extract_job_skills(
        job_description
    )

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

    # Store screening result for PDF report
    session["screening_data"] = {

    "name": name,
    "email": email,
    "phone": phone,

    "skills": list(resume_skills),

    "required_skills": list(required_skills),

    "matched_skills": list(matched_skills),

    "missing_skills": list(missing_skills),

    "skill_score": float(skill_score),

    "similarity_score": float(similarity_score),

    "final_score": float(final_score),

    "education": formatted_education,

    "experience": formatted_experience
}


    return render_template(
        "result.html",

        name=name,

        email=email,

        phone=phone,

        resume_skills=resume_skills,

        required_skills=required_skills,

        matched_skills=matched_skills,

        missing_skills=missing_skills,

        skill_score=skill_score,

        similarity_score=similarity_score,

        final_score=final_score,

        education=formatted_education,

        experience=formatted_experience
    )


@app.route("/download-report")
def download_report():

    data = session.get("screening_data")

    if not data:
        return "No screening result available.", 404

    filename = "resume_screening_report.pdf"

    generate_report(
        data,
        filename
    )

    return send_file(
        filename,
        as_attachment=True,
        download_name="resume_screening_report.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)