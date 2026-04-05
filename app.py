import gradio as gr
from datetime import datetime, timedelta
from fpdf import FPDF
import random

# Valid subjects (Hindi + English)
VALID_SUBJECTS = [
    "math", "science", "english", "hindi", "biology", "bio", "physics", "chemistry"
]

# Topic phases (to avoid repetition)
PHASES = ["Concept", "Practice", "Revision", "Test"]

def generate_plan(subject, hours_per_day, days, weak_topic):

    subject = subject.lower().strip()

    if subject not in VALID_SUBJECTS:
        return "Invalid subject (try Math, Science, Hindi, Bio)", None

    if hours_per_day <= 0 or days <= 0:
        return "Enter valid hours and days", None

    plan = []
    start_date = datetime.today()

    for i in range(days):
        date = (start_date + timedelta(days=i)).strftime("%d %b")
        phase = PHASES[i % len(PHASES)]

        topic_name = weak_topic if weak_topic else subject

        # slight variation in hours
        daily_hours = round(random.uniform(hours_per_day - 0.5, hours_per_day + 0.5), 1)

        line = f"{date}: {topic_name} ({phase}) - {daily_hours} hrs"
        plan.append(line)

    result = "Weekly Study Plan:\n\n" + "\n".join(plan)

    # 📄 PDF generation (NO EMOJI)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Study Plan Report", ln=True)

    for line in plan:
        pdf.multi_cell(0, 10, txt=line)

    pdf.output("study_plan.pdf")

    return result, "study_plan.pdf"


# UI
with gr.Blocks() as demo:
    gr.Markdown("# Study Planner AI")

    subject = gr.Textbox(label="Enter Subject (Math, Hindi, Bio...)")
    hours = gr.Number(label="Hours per Day", value=2)
    days = gr.Number(label="Number of Days", value=7)
    weak = gr.Textbox(label="Weak Topic (optional)")

    output_text = gr.Textbox(label="Your Plan")
    pdf_file = gr.File(label="Download PDF")

    btn = gr.Button("Generate Plan")

    btn.click(
        generate_plan,
        inputs=[subject, hours, days, weak],
        outputs=[output_text, pdf_file]
    )

demo.launch()
