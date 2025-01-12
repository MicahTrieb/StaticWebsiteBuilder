#!/usr/bin/env python3
import unittest
from blockmarkdown import markdown_to_html_node, block_to_blocktype, markdown_to_blocks

class TestBlocking(unittest.TestCase):
    def test_genericPrintTest(self):
        inputString = "# Welcome to My Markdown Example\n\nThis is a paragraph of text with some **bold** and *italic* formatting. Markdown is a lightweight markup language.\n\n## Features of Markdown\n\n1. **Simple Syntax** - Easy to learn and use.\n2. *Portable* - Works across platforms.\n3. Widely used in: stuff\n\n### Example Code Block\n\n```python\ndef hello_world():\n    print(\"Hello, World!\")\n```\n\n> **Tip**: Use Markdown to format your notes for better readability.\n\n### Resources\n\n- [Markdown Guide](https://www.markdownguide.org)\n- ![Example Image](https://via.placeholder.com/150)\n\n---\n\nThanks for checking out this example!\n"
        
        result = markdown_to_html_node(inputString)
        
        # Expected Outcome
        expected = {
            "tag": "div",
            "value": None,
            "children": [
                {"tag": "h1", "value": "Welcome to My Markdown Example", "children": None, "props": None},
                {"tag": "p", "value": "This is a paragraph of text with some **bold** and *italic* formatting. Markdown is a lightweight markup language.", "children": None, "props": None},
                {"tag": "h2", "value": "Features of Markdown", "children": None, "props": None},
                {"tag": "ol", "value": None, "children": [
                    {"tag": "li", "value": "1. **Simple Syntax** - Easy to learn and use.", "children": None, "props": None},
                    {"tag": "li", "value": "2. *Portable* - Works across platforms.", "children": None, "props": None},
                    {"tag": "li", "value": "3. Widely used in: stuff", "children": None, "props": None},
                ], "props": None},
                {"tag": "h3", "value": "Example Code Block", "children": None, "props": None},
                {"tag": "code", "value": "def hello_world():\n    print(\"Hello, World!\")", "children": None, "props": None},
                {"tag": "blockquote", "value": "**Tip**: Use Markdown to format your notes for better readability.", "children": None, "props": None},
                {"tag": "h3", "value": "Resources", "children": None, "props": None},
                {"tag": "ul", "value": None, "children": [
                    {"tag": "li", "value": None, "children": [
                        {"tag": "a", "value": "Markdown Guide", "children": None, "props": {"href": "https://www.markdownguide.org"}}
                    ], "props": None},
                    {"tag": "li", "value": None, "children": [
                        {"tag": "img", "value": None, "children": None, "props": {"src": "https://via.placeholder.com/150", "alt": "Example Image"}}
                    ], "props": None}
                ], "props": None},
                {"tag": "p", "value": "---", "children": None, "props": None},
                {"tag": "p", "value": "Thanks for checking out this example!", "children": None, "props": None}
            ],
            "props": None
        }
        print(result)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
