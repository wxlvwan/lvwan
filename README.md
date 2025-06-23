# Markdown Merge App

This repository contains a simple Flask application for merging markdown files.

## Usage

1. Install dependencies:
   ```bash
   python3 -m pip install flask markdown
   ```
2. Run the application:
   ```bash
   python3 merge_md_app.py
   ```
3. Visit `http://127.0.0.1:5000/` in your browser. You can select which markdown
   files from the current directory (including subdirectories) to merge and
   choose the name of the output HTML file.
4. The merged HTML content is saved to the chosen output file and also displayed
   in the browser.
