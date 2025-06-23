import os
from flask import Flask, request, render_template_string
import markdown

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def find_markdown_files(root):
    md_files = []
    for root_dir, dirs, files in os.walk(root):
        for f in files:
            if f.lower().endswith('.md'):
                md_files.append(os.path.relpath(os.path.join(root_dir, f), root))
    md_files.sort()
    return md_files


@app.route('/', methods=['GET'])
def index():
    files = find_markdown_files(BASE_DIR)
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Markdown Merger</title>
    </head>
    <body>
    <h1>Markdown Merger</h1>
    <form method="POST" action="/merge">
        <label>Output HTML file name:
            <input type="text" name="output" value="merged.html" />
        </label>
        <h3>Select markdown files to merge:</h3>
        {% for file in files %}
            <div>
                <input type="checkbox" name="files" value="{{ file }}" checked />
                <label>{{ file }}</label>
            </div>
        {% endfor %}
        <button type="submit">Merge Selected</button>
    </form>
    </body>
    </html>
    '''
    return render_template_string(html, files=files)


@app.route('/merge', methods=['POST'])
def merge():
    selected_files = request.form.getlist('files')
    output_name = request.form.get('output', 'merged.html')
    contents = []
    for path in selected_files:
        abs_path = os.path.join(BASE_DIR, path)
        with open(abs_path, 'r', encoding='utf-8') as f:
            contents.append(f.read())
    combined_md = '\n\n'.join(contents)
    html_body = markdown.markdown(combined_md)
    html_result = f"<html><body>{html_body}</body></html>"
    output_path = os.path.join(BASE_DIR, output_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_result)
    return html_result


if __name__ == '__main__':
    app.run(debug=True)
