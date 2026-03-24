ExamAnalytics

CLI tool for generating reports from CSV files with student exam data.

Supported reports:
- median-coffee

Installation:

pip install -e .

Example:

python -m examanalytics.main --files data/math.csv data/physics.csv --report median-coffee