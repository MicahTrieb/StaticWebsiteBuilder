#!/usr/bin/env python3
import unittest
from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_extractTitleWithHeader(self):
        inputText = "# This has a header"
        expectedOutput = "This has a header"
        function = extract_title(inputText)
        self.assertEqual(function, expectedOutput)

    def test_extractWithNoHeader(self):
        inputText = "This should raise an exception"
        with self.assertRaises(Exception):
            extract_title(inputText)

    def test_wrongly_formatted_header(self):
        inputText = "### This has three hashes instead of one"
        with self.assertRaises(Exception):
            extract_title(inputText)

        
if __name__ == "__main__":
    unittest.main()