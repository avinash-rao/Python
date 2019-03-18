from docx import Document

document = Document('Avinash vb.docx')
fullText = []
for para in document.paragraphs:
    fullText.append(para.text)

print('\n'.join(fullText))