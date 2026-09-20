import os

import markdown


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_PATH = os.path.join(BASE_DIR, "Computer_Vision_Competition_10_Day_Workbook.md")
CSS_PATH = os.path.join(BASE_DIR, "workbook.css")
HTML_PATH = os.path.join(BASE_DIR, "Computer_Vision_Competition_10_Day_Workbook.html")
PDF_PATH = os.path.join(BASE_DIR, "Computer_Vision_Competition_10_Day_Workbook.pdf")

with open(SOURCE_PATH, encoding="utf-8") as handle:
    source = handle.read()

with open(CSS_PATH, encoding="utf-8") as handle:
    css = handle.read()

body = markdown.markdown(
    source,
    extensions=["tables", "fenced_code", "sane_lists", "md_in_html"],
    output_format="html5",
)

document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Computer Vision Competition — 10-Day Offline Workbook</title>
<style>{css}</style>
</head>
<body>{body}</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as handle:
    handle.write(document)

print(HTML_PATH)
print(PDF_PATH)
