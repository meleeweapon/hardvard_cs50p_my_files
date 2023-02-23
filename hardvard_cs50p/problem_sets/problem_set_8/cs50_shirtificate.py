from fpdf import FPDF

def main() -> None:
  user_input = "awooga"

  pdf = FPDF(orientation="portrait", format="A4")
  pdf.add_page()
  pdf.set_font("helvetica", "B", 64)
  print(pdf.x)
  pdf.cell(190, 10, "CS50 Shirtificate", align='C')
  print(pdf.x)
  pdf.image("shirtificate.png", 0, 40)
  pdf.set_text_color(255, 255, 255)
  pdf.set_font("helvetica", "B", 32)
  pdf.cell(-190, 210, f"{user_input} took CS50", align='C')
  pdf.output("tutorial.pdf")


if __name__ == '__main__':
  main()