<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:%23a78bfa&height=170&section=header&text=HTML%20TABLE%20EXTRACT&fontSize=38&fontColor=ffffff" alt="HTML Table Extract banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=22&pause=1000&color=A78BFA&center=true&vCenter=true&width=650&lines=Extract+local+HTML+tables+into+CSV+or+JSON" alt="Typing title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/html-table-extract"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/html-table-extract"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/html-table-extract"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/html-table-extract"/></p>
<p align="center"><img src="assets/overview.svg" alt="HTML Table Extract illustration" width="92%"/></p>

## 🧭 Overview
HTML Table Extract reads saved HTML files and exports their top-level tables as CSV or JSON. It works offline and never uploads documents.

## ✨ Features
- 📋 Extracts rows and cells from top-level HTML tables.
- 📤 Exports a selected table as CSV or JSON.
- 🧱 Pads uneven rows for consistent output.
- 🔒 Uses Python's standard library.

## 🎬 Demo
```text
$ python main.py examples/report.html --format csv
Name,Status,Count
Alpha,Ready,12
Beta,Review,8
```
This is a local example, not a hosted demo.

## 🚀 Quick Start
```bash
python -m pip install -r requirements.txt
python main.py examples/report.html --format csv
```
Use `--table 2` to select the second table and `--output result.csv` to write a file.

## 🧰 Tech Stack
- Python 3.10+
- html.parser, csv, and json from the standard library
- unittest

## 🗂️ Folder Structure
```text
main.py
table_extract.py
tests/test_table_extract.py
examples/report.html
assets/overview.svg
requirements.txt
```

## 🗺️ Roadmap
- [x] Top-level table extraction
- [x] CSV and JSON export
- [ ] Optional handling for row and column spans

## 🤝 Contributing
Issues and focused pull requests are welcome. Add regression tests for parser edge cases.

## 📄 License
Released under the [MIT License](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:%23a78bfa&height=110&section=footer" alt="Animated footer"/></p>
