#!/usr/bin/env python3
from regexfunction import extract_markdown_images
import unittest


class testRegex(unittest.TestCase):
    def test_rickAstley(self):
        rickRoll = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expectedOutcome = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
]
        testingFunction = extract_markdown_images(rickRoll)
        self.assertEqual(testingFunction, expectedOutcome)

    def test_notaTest_(self):
        rickRoll = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        #print(extract_markdown_images(rickRoll))    
if __name__ == "__main__":
    unittest.main()
    