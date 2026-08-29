import re


def extract_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    email = re.search(email_pattern, text)

    if email:
        return email.group()

    return "Not found"


def extract_phone(text):
    phone_pattern = r'(?:\+91[\s-]?)?[6-9]\d{9}'

    phone = re.search(phone_pattern, text)

    if phone:
        return phone.group()

    return "Not found"


SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "mysql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "power bi",
    "tableau",
    "excel",
    "statistics",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "flask",
    "django",
    "html",
    "css",
    "javascript",
    "react",
    "git",
    "github"
]


SKILL_ALIASES = {
    "ml": "machine learning",
    "machine-learning": "machine learning",

    "powerbi": "power bi",
    "power-bi": "power bi",

    "num py": "numpy",

    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",

    "js": "javascript"
}


def extract_skills(text):
    text = text.lower()

    found_skills = set()

    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    for alias, standard_skill in SKILL_ALIASES.items():
        if alias in text:
            found_skills.add(standard_skill)

    return list(found_skills)

def extract_education(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    education_headings = [
        "education",
        "academic qualification",
        "educational qualification",
        "academics"
    ]

    section_end_headings = [
        "experience",
        "work experience",
        "professional experience",
        "skills",
        "technical skills",
        "projects",
        "certifications",
        "achievements",
        "internship",
        "contact",
        "objective",
        "summary",
        "profile"
    ]

    education_lines = []
    inside_education = False

    for line in lines:
        line_lower = line.lower()

        if line_lower in education_headings:
            inside_education = True
            continue

        if inside_education and line_lower in section_end_headings:
            break

        if inside_education:
            education_lines.append(line)

    return education_lines


def format_education(education_lines):
    if not education_lines:
        return ["No education information found"]

    formatted = []
    current_entry = []

    for line in education_lines:

        degree_keywords = [
            "b.tech",
            "btech",
            "b.e",
            "be ",
            "m.tech",
            "mtech",
            "m.e",
            "me ",
            "mca",
            "bca",
            "b.sc",
            "bsc",
            "m.sc",
            "msc",
            "mba",
            "hsc",
            "class xii",
            "class x",
            "sslc"
        ]

        is_new_entry = any(
            keyword in line.lower()
            for keyword in degree_keywords
        )

        if is_new_entry and current_entry:
            formatted.append(current_entry)
            current_entry = []

        current_entry.append(line)

    if current_entry:
        formatted.append(current_entry)

    return formatted


def extract_experience(text):

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    start_headings = [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history",
        "career history"
    ]

    stop_headings = [
        "education",
        "education and training",
        "academic background",
        "skills",
        "additional skills",
        "technical skills",
        "certifications",
        "certification",
        "projects",
        "achievements",
        "references",
        "declaration"
    ]

    # Find the Experience section
    start_index = -1

    for i, line in enumerate(lines):

        if line.lower().strip() in start_headings:
            start_index = i + 1
            break

    # No Experience section
    if start_index == -1:
        return []

    # Find where Experience section ends
    end_index = len(lines)

    for i in range(start_index, len(lines)):

        if lines[i].lower().strip() in stop_headings:
            end_index = i
            break

    experience_lines = lines[start_index:end_index]

    return parse_experience_entries(experience_lines)


def parse_experience_entries(lines):

    entries = []

    # Matches formats such as:
    #
    # 08/2016 – Present
    # 03/2012 - 07/2016
    # Jun 2023 – Dec 2023
    # 2022 – Present
    # 2019 to 2022

    date_pattern = re.compile(
        r"""
        (
            (?:
                Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|
                January|February|March|April|May|June|
                July|August|September|October|November|December
            )
            \s+\d{4}
            |
            \d{1,2}/\d{4}
            |
            \d{4}
        )
        \s*
        (?:-|–|—|to)
        \s*
        (
            (?:
                Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|
                January|February|March|April|May|June|
                July|August|September|October|November|December
            )
            \s+\d{4}
            |
            \d{1,2}/\d{4}
            |
            \d{4}
            |
            Present|Current
        )
        """,
        re.IGNORECASE | re.VERBOSE
    )

    # Headings that should never become job roles
    invalid_roles = [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history",
        "education",
        "skills",
        "projects",
        "certifications",
        "achievements",
        "references"
    ]

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        # Ignore common resume table headings
        if line.lower() in [
            "total years",
            "last used",
            "accomplishments",
            "responsibilities",
            "responsibility",
            "duties",
            "job duties"
        ]:
            i += 1
            continue

        # ==================================================
        # FORMAT 1
        #
        # Data Analyst Intern
        # Insight Analytics Pvt Ltd | Jun 2023 – Dec 2023
        # ==================================================

        if i + 1 < len(lines):

            next_line = lines[i + 1]

            match = date_pattern.search(next_line)

            if match:

                role = line

                company_part = next_line[:match.start()].strip()

                date = match.group(0).strip()

                company = company_part.strip(" |,-–—")

                # Make sure this is not a section heading
                if (
                    len(role) > 2
                    and role.lower() not in invalid_roles
                ):

                    entries.append({
                        "role": role,
                        "company": company,
                        "date": date
                    })

                    i += 2
                    continue

        # ==================================================
        # FORMAT 2
        #
        # Company Name City, State Information Technology
        # Specialist
        # 08/2013 to 02/2016
        # ==================================================

        match = date_pattern.search(line)

        if match:

            before_date = line[:match.start()].strip()

            date = match.group(0).strip()

            role = before_date

            company = ""

            # Handle "Company Name"
            if "company name" in before_date.lower():

                remaining = re.sub(
                    r"company name",
                    "",
                    before_date,
                    flags=re.IGNORECASE
                ).strip()

                role_keywords = [
                    "specialist",
                    "analyst",
                    "developer",
                    "engineer",
                    "intern",
                    "administrator",
                    "manager",
                    "assistant",
                    "technician",
                    "support"
                ]

                role_start = None

                for keyword in role_keywords:

                    role_match = re.search(
                        rf"\b[\w /()-]*{keyword}[\w /()-]*\b",
                        remaining,
                        re.IGNORECASE
                    )

                    if role_match:

                        role_start = role_match.start()
                        break

                if role_start is not None:

                    company = remaining[:role_start].strip(" ,-")

                    role = remaining[role_start:].strip()

                else:

                    role = remaining

            # Don't add empty or invalid roles
            if (
                len(role) > 2
                and role.lower() not in invalid_roles
            ):

                entries.append({
                    "role": role,
                    "company": company,
                    "date": date
                })

            i += 1
            continue

        i += 1

    return entries


def format_experience(experience):

    return experience

def extract_name(text):
    lines = text.strip().split("\n")

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if "@" in line or any(char.isdigit() for char in line):
            continue

        skip_words = [
            "resume",
            "curriculum vitae",
            "education",
            "skills",
            "projects",
            "experience",
            "objective",
            "profile",
            "summary",
            "contact",
            "phone",
            "email",
            "linkedin",
            "github",
            "college",
            "university",
            "engineering"
        ]

        if any(word in line.lower() for word in skip_words):
            continue

        words = line.split()

        if 2 <= len(words) <= 4:
            return line

    return "Not found"