from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('images/system_1.png', x=50, y=100, w=150, h=100)

pdf.set_font('Arial', 'B', 24)

pdf.cell(w=0, h=50, txt='LLM Attacks', ln=True, align='C', border=1)

pdf.set_xy(50, 200)

pdf.set_font('Arial','', 12)
text = """LLM attacks are techniques used to manipulate or exploit large language models, potentially causing them to produce unsafe, incorrect, or unintended outputs. Common examples include prompt injection, jailbreaks, data poisoning, and adversarial inputs. Understanding these attacks helps developers build stronger safeguards, improve model reliability, and protect AI systems from misuse."""


pdf.multi_cell(w=0, h=18, txt=text)
pdf.set_xy(50, 300)
# pdf.set_font('Arial', 'B', 12)
# pdf.cell(w=100, h=15, txt='References:')

# pdf.set_font('Arial', '', 12)
# pdf.cell(w=100, h=15, txt='https://arxiv.org/abs/2302.11382')

pdf.write(
    18,
    "Learn more about LLM security at "
)

pdf.set_text_color(0, 0, 255)

pdf.write(
    18,
    "OWASP",
    "https://owasp.org/www-project-top-10-for-large-language-model-applications/"
)

pdf.output('output.pdf')