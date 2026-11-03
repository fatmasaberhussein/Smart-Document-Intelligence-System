import unittest

from main import analyze_document


class TestDocumentAnalyzer(unittest.TestCase):

    def test_word_count(self):
        content = "Python is easy and useful."

        result = analyze_document(content)

        self.assertEqual(result["word_count"], 5)

    def test_character_count(self):
        content = "Python"

        result = analyze_document(content)

        self.assertEqual(result["character_count"], 6)

    def test_sentence_count(self):
        content = "Hello. How are you? Great!"

        result = analyze_document(content)

        self.assertEqual(result["sentence_count"], 3)

    def test_empty_document(self):
        content = ""

        result = analyze_document(content)

        self.assertEqual(result["word_count"], 0)
        self.assertEqual(result["character_count"], 0)
        self.assertEqual(result["sentence_count"], 0)

if __name__ == "__main__":
    unittest.main()