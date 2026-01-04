import markdown
import pdfkit

with open("names.md", "r", encoding="utf-8") as f:
    md_file = f.read()

html_file = markdown.markdown(md_file)

pdfkit.from_string(html_file, "names.pdf")

print("PDF created successfuly")
