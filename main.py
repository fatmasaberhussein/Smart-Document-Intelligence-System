
import os
import csv


# =====================================
# 1. Project Paths
# =====================================

DOCUMENTS_FOLDER = "documents"
REPORTS_FOLDER = "reports"


# =====================================
# 2. Document Manager
# =====================================

def get_documents():
    """Find all TXT documents."""

    if not os.path.exists(DOCUMENTS_FOLDER):
        print("Documents folder not found.")
        return []

    document_names = os.listdir(DOCUMENTS_FOLDER)

    text_documents = []

    for document_name in document_names:
        if document_name.endswith(".txt"):
            text_documents.append(document_name)

    return text_documents


def read_document(document_name):
    """Read a document and return its content."""

    file_path = os.path.join(DOCUMENTS_FOLDER, document_name)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content

    except FileNotFoundError:
        print(f"Document not found: {document_name}")

    except UnicodeDecodeError:
        print(f"Cannot read document encoding: {document_name}")

    except OSError:
        print(f"Could not read document: {document_name}")

    return None


# =====================================
# 3. Text Analyzer
# =====================================

def analyze_document(content):
    """Analyze document text."""

    words = content.split()
    word_count = len(words)

    character_count = len(content)

    dots = content.count(".")
    exclamations = content.count("!")
    questions = content.count("?")

    sentence_count = dots + exclamations + questions

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "character_count": character_count
    }


# =====================================
# 4. Search Engine
# =====================================

def search_keyword(content, keyword):
    """Count keyword occurrences."""

    occurrence_count = content.lower().count(keyword.lower())

    return occurrence_count


# =====================================
# 5. Report Generator
# =====================================

def generate_report(document_name, analysis_result, occurrence_count):

    report = {
        "document_name": document_name,
        "word_count": analysis_result["word_count"],
        "sentence_count": analysis_result["sentence_count"],
        "character_count": analysis_result["character_count"],
        "occurrence_count": occurrence_count
    }

    return report


def display_report(report):

    print("\n========== Document Report ==========")

    print(f"Document: {report['document_name']}")
    print(f"Words: {report['word_count']}")
    print(f"Sentences: {report['sentence_count']}")
    print(f"Characters: {report['character_count']}")
    print(f"Keyword occurrences: {report['occurrence_count']}")

    print("=====================================\n")


# =====================================
# 6. Save Text Reports
# =====================================

def save_text_report(report):

    os.makedirs(REPORTS_FOLDER, exist_ok=True)

    report_text = f"""
Research Report

Document: {report['document_name']}
Words: {report['word_count']}
Sentences: {report['sentence_count']}
Characters: {report['character_count']}
Keyword occurrences: {report['occurrence_count']}
"""

    report_path = os.path.join(
        REPORTS_FOLDER,
        report["document_name"] + "_report.txt"
    )

    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write(report_text)

        print(f"Report saved: {report_path}")

    except OSError:
        print("Could not save the report.")


# =====================================
# 7. Export Results to CSV
# =====================================

def export_to_csv(all_results):

    os.makedirs(REPORTS_FOLDER, exist_ok=True)

    csv_path = os.path.join(REPORTS_FOLDER, "all_reports.csv")

    try:
        with open(csv_path, "w", newline="", encoding="utf-8-sig") as file:

            field_names = [
                "document_name",
                "word_count",
                "sentence_count",
                "character_count",
                "occurrence_count"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=field_names
            )

            writer.writeheader()
            writer.writerows(all_results)

        print(f"CSV report saved: {csv_path}")

    except OSError:
        print("Could not export CSV report.")


# =====================================
# 8. Main Program
# =====================================

def main():

    print("=" * 45)
    print(" SMART DOCUMENT INTELLIGENCE SYSTEM ")
    print("=" * 45)

    document_names = get_documents()

    if not document_names:
        print("No TXT documents found.")
        return

    keyword = input("\nEnter a keyword to search for: ").strip()

    if not keyword:
        print("Keyword cannot be empty.")
        return

    all_results = []

    for document_name in document_names:

        print(f"\nProcessing: {document_name}")

        content = read_document(document_name)

        if content is None:
            continue

        analysis_result = analyze_document(content)

        occurrence_count = search_keyword(content, keyword)

        report = generate_report(
            document_name,
            analysis_result,
            occurrence_count
        )

        display_report(report)

        save_text_report(report)

        all_results.append(report)

    if all_results:
        export_to_csv(all_results)

        total_words = 0

        for result in all_results:
            total_words += result["word_count"]

        print("\n========== Final Summary ==========")
        print(f"Documents processed: {len(all_results)}")
        print(f"Total words: {total_words}")
        print(f"Keyword searched: {keyword}")
        print("===================================")

    else:
        print("No documents were processed successfully.")


# =====================================
# 9. Program Entry Point
# =====================================

if __name__ == "__main__":
    main()
