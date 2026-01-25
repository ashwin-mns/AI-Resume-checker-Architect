from fpdf import FPDF

def generate_resume_pdf(content, output_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    # Sanitize for latin-1
    content = content.replace("•", "-").replace("—", "-").replace("’", "'").replace("“", '"').replace("”", '"')
    content = content.encode('latin-1', 'replace').decode('latin-1')

    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(output_file)
    return output_file
