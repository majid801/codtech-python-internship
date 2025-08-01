import csv
from fpdf import FPDF

def analyze_csv(file_path):
    students = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            maths = int(row['Maths'])
            science = int(row['Science'])
            english = int(row['English'])
            total = maths + science + english
            avg = total / 3
            students.append((name, maths, science, english, total, avg))
    return students

def generate_pdf(data, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Student Marks Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, "Name", 1)
    pdf.cell(25, 10, "Maths", 1)
    pdf.cell(25, 10, "Science", 1)
    pdf.cell(25, 10, "English", 1)
    pdf.cell(25, 10, "Total", 1)
    pdf.cell(25, 10, "Average", 1)
    pdf.ln()

    for student in data:
        name, maths, science, english, total, avg = student
        pdf.cell(40, 10, name, 1)
        pdf.cell(25, 10, str(maths), 1)
        pdf.cell(25, 10, str(science), 1)
        pdf.cell(25, 10, str(english), 1)
        pdf.cell(25, 10, str(total), 1)
        pdf.cell(25, 10, f"{avg:.2f}", 1)
        pdf.ln()

    pdf.output(output_path)
    print(f"✅ PDF report saved as: {output_path}")

# Run the script
csv_file = "students.csv"
pdf_file = "student_report.pdf"

data = analyze_csv(csv_file)
generate_pdf(data, pdf_file)
