from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch


def generate_report(data, filename):

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=20,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=13,
        spaceBefore=14,
        spaceAfter=8
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["Normal"],
        fontSize=10,
        leading=14
    )

    small_style = ParagraphStyle(
        "SmallStyle",
        parent=styles["Normal"],
        fontSize=9,
        leading=12
    )

    # Style for job/degree titles
    item_title_style = ParagraphStyle(
        "ItemTitleStyle",
        parent=styles["Normal"],
        fontSize=11,
        leading=14,
        spaceAfter=3
    )

    story = []

    # =========================================
    # TITLE
    # =========================================

    story.append(
        Paragraph(
            "RESUME SCREENING REPORT",
            title_style
        )
    )

    # =========================================
    # CANDIDATE INFORMATION
    # =========================================

    story.append(
        Paragraph(
            "Candidate Information",
            heading_style
        )
    )

    candidate_data = [
        ["Name", str(data.get("name", "Not found"))],
        ["Email", str(data.get("email", "Not found"))],
        ["Phone", str(data.get("phone", "Not found"))]
    ]

    candidate_table = Table(
        candidate_data,
        colWidths=[1.2 * inch, 5.8 * inch]
    )

    candidate_table.setStyle(
        TableStyle([
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
        ])
    )

    story.append(candidate_table)

    # =========================================
    # EDUCATION
    # =========================================

    story.append(
        Paragraph(
            "Education",
            heading_style
        )
    )

    education = data.get("education", [])

    if education:

        for item in education:

            # If education is a dictionary
            if isinstance(item, dict):

                degree = item.get(
                    "degree",
                    item.get("qualification", "Education")
                )

                institution = item.get(
                    "institution",
                    item.get("college", "")
                )

                year = item.get(
                    "year",
                    item.get("duration", "")
                )

                cgpa = item.get(
                    "cgpa",
                    ""
                )

                story.append(
                    Paragraph(
                        f"<b>{degree}</b>",
                        item_title_style
                    )
                )

                if institution:

                    story.append(
                        Paragraph(
                            str(institution),
                            normal_style
                        )
                    )

                if year:

                    story.append(
                        Paragraph(
                            str(year),
                            small_style
                        )
                    )

                if cgpa:

                    story.append(
                        Paragraph(
                            f"CGPA: {cgpa}",
                            small_style
                        )
                    )

                story.append(
                    Spacer(1, 8)
                )

            else:

                # If education is already formatted text
                story.append(
                    Paragraph(
                        str(item).replace("\n", "<br/>"),
                        normal_style
                    )
                )

                story.append(
                    Spacer(1, 8)
                )

    else:

        story.append(
            Paragraph(
                "No education information found.",
                normal_style
            )
        )

    # =========================================
    # EXPERIENCE
    # =========================================

    story.append(
        Paragraph(
            "Experience",
            heading_style
        )
    )

    experience = data.get("experience", [])

    if experience:

        for job in experience:

            # Dictionary format
            if isinstance(job, dict):

                role = job.get(
                    "role",
                    "Role not found"
                )

                company = job.get(
                    "company",
                    ""
                )

                date = job.get(
                    "date",
                    ""
                )

                story.append(
                    Paragraph(
                        f"<b>{role}</b>",
                        item_title_style
                    )
                )

                if company:

                    story.append(
                        Paragraph(
                            str(company),
                            normal_style
                        )
                    )

                if date:

                    story.append(
                        Paragraph(
                            str(date),
                            small_style
                        )
                    )

                story.append(
                    Spacer(1, 8)
                )

            else:

                story.append(
                    Paragraph(
                        str(job).replace("\n", "<br/>"),
                        normal_style
                    )
                )

                story.append(
                    Spacer(1, 8)
                )

    else:

        story.append(
            Paragraph(
                "No professional experience found.",
                normal_style
            )
        )

    # =========================================
    # RESUME SKILLS
    # =========================================

    story.append(
        Paragraph(
            "Resume Skills",
            heading_style
        )
    )

    resume_skills = data.get(
        "skills",
        []
    )

    if resume_skills:

        for skill in resume_skills:

            story.append(
                Paragraph(
                    f"• {skill}",
                    normal_style
                )
            )

    else:

        story.append(
            Paragraph(
                "No skills found.",
                normal_style
            )
        )

    # =========================================
    # REQUIRED SKILLS
    # =========================================

    story.append(
        Paragraph(
            "Required Skills",
            heading_style
        )
    )

    required_skills = data.get(
        "required_skills",
        []
    )

    if required_skills:

        for skill in required_skills:

            story.append(
                Paragraph(
                    f"• {skill}",
                    normal_style
                )
            )

    # =========================================
    # MATCHED SKILLS
    # =========================================

    story.append(
        Paragraph(
            "Matched Skills",
            heading_style
        )
    )

    matched_skills = data.get(
        "matched_skills",
        []
    )

    if matched_skills:

        for skill in matched_skills:

            story.append(
                Paragraph(
                    f"✓ {skill}",
                    normal_style
                )
            )

    else:

        story.append(
            Paragraph(
                "No matched skills.",
                normal_style
            )
        )

    # =========================================
    # MISSING SKILLS
    # =========================================

    story.append(
        Paragraph(
            "Missing Skills",
            heading_style
        )
    )

    missing_skills = data.get(
        "missing_skills",
        []
    )

    if missing_skills:

        for skill in missing_skills:

            story.append(
                Paragraph(
                    f"✗ {skill}",
                    normal_style
                )
            )

    else:

        story.append(
            Paragraph(
                "No missing skills.",
                normal_style
            )
        )

    # =========================================
    # SCREENING SCORES
    # =========================================

    story.append(
        Paragraph(
            "Screening Scores",
            heading_style
        )
    )

    skill_score = data.get(
        "skill_score",
        0
    )

    similarity_score = data.get(
        "similarity_score",
        0
    )

    final_score = data.get(
        "final_score",
        0
    )

    score_data = [
        [
            "Skill Match Score",
            f"{skill_score:.2f}%"
        ],
        [
            "Text Similarity Score",
            f"{similarity_score:.2f}%"
        ],
        [
            "Final Match Score",
            f"{final_score:.2f}%"
        ]
    ]

    score_table = Table(
        score_data,
        colWidths=[
            4.5 * inch,
            2.5 * inch
        ]
    )

    score_table.setStyle(
        TableStyle([
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),

            ("FONTNAME",
             (0, -1),
             (-1, -1),
             "Helvetica-Bold"),

            ("FONTSIZE",
             (0, 0),
             (-1, -1),
             10),

            ("ALIGN",
             (1, 0),
             (1, -1),
             "CENTER"),

            ("VALIGN",
             (0, 0),
             (-1, -1),
             "MIDDLE"),

            ("GRID",
             (0, 0),
             (-1, -1),
             0.5,
             colors.grey),

            ("TOPPADDING",
             (0, 0),
             (-1, -1),
             8),

            ("BOTTOMPADDING",
             (0, 0),
             (-1, -1),
             8),
        ])
    )

    story.append(score_table)

    # =========================================
    # FOOTER
    # =========================================

    story.append(
        Spacer(1, 30)
    )

    story.append(
        Paragraph(
            "Generated by Resume Screening System",
            small_style
        )
    )

    # Build PDF
    doc.build(story)