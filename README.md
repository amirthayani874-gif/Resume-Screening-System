# Resume Screening System

A web-based Resume Screening System built using Python and Flask.

The system allows users to upload a resume and provide a job description. It extracts important information from the resume and compares the candidate's skills with the skills required for the job.

## Features

- Resume PDF upload
- Extract candidate name, email and phone number
- Extract skills from resumes
- Extract education details
- Extract work experience
- Extract required skills from job descriptions
- Compare resume skills with job requirements
- Identify matched and missing skills
- Calculate Skill Match Score
- Calculate Text Similarity Score
- Calculate Final Match Score
- Generate downloadable PDF screening reports
- Simple and user-friendly web interface

## Technologies Used

- Python
- Flask
- PyMuPDF
- Scikit-learn
- ReportLab
- HTML
- CSS

## Project Structure

Resume-Screening-System/
│
├── app.py
├── resume_parser.py
├── resume_info.py
├── job_matcher.py
├── similarity.py
├── report_generator.py
├── requirements.txt
├── job_description.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── test_info.py
├── test_job.py
├── test_parser.py
└── test_similarity.py

## How It Works

Upload Resume
      ↓
Extract Resume Text
      ↓
Extract Candidate Information
      ↓
Extract Skills, Education & Experience
      ↓
Enter Job Description
      ↓
Extract Required Skills
      ↓
Compare Resume & Job Requirements
      ↓
Calculate Match Scores
      ↓
Display Screening Result
      ↓
Download PDF Report


## Screening Process

The system provides three main scores:

**Skill Match Score**

Measures how many of the required job skills are found in the resume.

**Text Similarity Score**

Measures the similarity between the resume content and the job description.

**Final Match Score**

Combines the screening scores to provide an overall candidate-job match score.

## Future Improvements

Improve resume parsing for complex resume formats
Add skill aliases and synonyms
Improve experience extraction
Add advanced NLP-based matching
Add candidate ranking
Add multiple-resume comparison
Improve score visualization
Deploy the application online

## Disclaimer

This project is developed as a mini-project for educational purposes. The screening score should be used as an assisting tool and not as the sole basis for hiring decisions.

## Author

Sathya Varshaa S. T

B.Tech Artificial Intelligence and Data Science