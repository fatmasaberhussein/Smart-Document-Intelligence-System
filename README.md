# Smart Document Intelligence System

A Python-based application designed to help students and researchers manage and analyze text documents.

## Features

- Read multiple TXT documents.
- Count words, sentences, and characters.
- Search for keywords across documents.
- Generate individual text reports.
- Export analysis results to CSV.
- Handle common file-reading errors.
- Run automated tests using Python unittest.

## Project Structure

```text
Smart_Document_Intelligence_System/
│
├── main.py
├── documents/
│   ├── research.txt
│   └── ai_research.txt
├── reports/
├── tests/
│   └── test_analyzer.py
└── README.md
```

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

1. Clone or download the project.
2. Open the project folder in your terminal.
3. Run:

```bash
python main.py
```

4. Enter a keyword when prompted.

## How to Run Tests

Run the following command:

```bash
python -m unittest discover -s tests -v
```

## Technologies Used

- Python
- File Handling
- Dictionaries and Lists
- Functions
- Exception Handling
- CSV
- Unit Testing

## Project Status

Version 1 – Working MVP

## Future Improvements

- PDF document support.
- Database integration.
- Improved text analysis.
- AI-powered document summarization.
- Intelligent document classification.

## Author

Fatma