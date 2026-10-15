from flask import Flask, render_template, request
from pathlib import Path
import os

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
GALLERY_DIR = BASE_DIR / "static" / "gallery"
GALLERY_DIR.mkdir(parents=True, exist_ok=True)
ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "gif"}

PROFILE = {
    "name": "T G NARAYANAN",
    "degree": "M.Sc. Electronics",
    "headline": "STEM Trainer | Electronics Graduate | Robotics, Embedded Systems & IoT Project Developer",
    "location": "Paramakudi, Ramanathapuram District, Tamil Nadu, India",
    "email": "tgnarayananmsc@gmail.com",
    "dob": "04 December 2002",
    "gender": "Male",
    "languages": ["Sourashtra", "Tamil", "English"],
    "education": [
        {"year": "2025", "degree": "M.Sc. Electronics", "status": "Postgraduate completed"},
        {"year": "2023", "degree": "B.Sc. Electronics", "status": "Undergraduate completed"},
    ],
    "experience": [
        {"title": "STEM Trainer", "description": "Hands-on STEM learning, electronics demonstrations, and practical project guidance."}
    ],
    "projects": [
        {
            "category": "UG Final-Year Project",
            "title": "RFID-Based Real-Time Attendance System",
            "description": "An attendance system concept using RFID identification and real-time attendance recording."
        },
        {
            "category": "PG Final-Year Project",
            "title": "ANPR-Based Smart Toll Payment & Vehicle Management System",
            "description": "A vehicle-management project concept using Automatic Number Plate Recognition (ANPR) for smart toll workflows."
        },
        {
            "category": "Project Development",
            "title": "Robotics, Embedded Systems, IoT & Computer Science Projects",
            "description": "Practical project design, prototyping, electronics integration, and STEM project support."
        },
    ],
}

@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE)

@app.route("/resume")
def resume():
    return render_template("resume.html", profile=PROFILE)

@app.route("/project-request", methods=["GET", "POST"])
def project_request():
    if request.method == "POST":
        # Static-site visitors can use the email button instead. This Flask form
        # intentionally prepares a mailto message rather than storing personal data.
        fields = {
            "name": request.form.get("name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "project_type": request.form.get("project_type", "").strip(),
            "budget": request.form.get("budget", "").strip(),
            "deadline": request.form.get("deadline", "").strip(),
            "requirements": request.form.get("requirements", "").strip(),
        }
        if not fields["name"] or not fields["requirements"]:
            flash("Please enter your name and project requirements.", "error")
            return render_template("project_request.html", profile=PROFILE, values=fields)
        import urllib.parse
        subject = f"Project enquiry from {fields['name']} - {fields['project_type'] or 'Project'}"
        body = (
            f"Name: {fields['name']}\nEmail: {fields['email']}\n"
            f"Project type: {fields['project_type']}\nBudget: {fields['budget']}\n"
            f"Expected timeline: {fields['deadline']}\n\nRequirements:\n{fields['requirements']}"
        )
        mailto = "mailto:" + PROFILE["email"] + "?" + urllib.parse.urlencode({
            "subject": subject, "body": body
        })
        return render_template("email_ready.html", profile=PROFILE, mailto=mailto)
    return render_template("project_request.html", profile=PROFILE, values={})

@app.route("/gallery")
def gallery():
    images = sorted(
        [
            p.name for p in GALLERY_DIR.iterdir()
            if p.is_file() and p.suffix.lower().lstrip(".") in ALLOWED_IMAGE_EXTENSIONS
        ],
        key=str.lower
    )
    return render_template("gallery.html", profile=PROFILE, images=images)

if __name__ == "__main__":
    # Local development only. Do not expose Flask's debug server to the internet.
    app.run(host="127.0.0.1", port=5000, debug=True)
