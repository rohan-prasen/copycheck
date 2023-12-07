import docx
from io import TextIOWrapper
from flask import flash

def check_copy(file):
    if not file:
        flash('No file provided.')
        return None

    filename = file.filename.lower()
    if filename.endswith('.txt'):
        content = file.read().decode('utf-8')
    elif filename.endswith('.docx'):
        content = read_docx(file)
    else:
        flash('Invalid file format. Only .txt and .docx are supported.')
        return None

    # Implement your copy-checking logic here
    # For simplicity, let's just check if the text contains "copy"
    result = content.lower().find('copy') != -1

    return result

def read_docx(file):
    doc = docx.Document(file)
    content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    return content
