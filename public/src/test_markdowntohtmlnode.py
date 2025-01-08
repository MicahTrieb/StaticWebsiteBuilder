#!/usr/bin/env python3
import unittest
from blockmarkdown import markdown_to_html_node, block_to_blocktype, markdown_to_blocks


class TestBlocking(unittest.TestCase):
    def test_genericPrintTest(self):
        
        a = markdown_to_html_node("# Welcome to My Markdown Example\n\nThis is a paragraph of text with some **bold** and *italic* formatting. Markdown is a lightweight markup language.\n\n## Features of Markdown\n\n1. **Simple Syntax** - Easy to learn and use.\n2. *Portable* - Works across platforms.\n3. Widely used in:\n   - Documentation\n   - Blogging\n   - Note-taking\n\n### Example Code Block\n\n```python\n\ndef hello_world():\n    print(\"Hello, World!\")\n```\n\n> **Tip**: Use Markdown to format your notes for better readability.\n\n### Resources\n- [Markdown Guide](https://www.markdownguide.org)\n- ![Example Image](https://via.placeholder.com/150)\n\n---\n\nThanks for checking out this example!\n")
        print(a)
if __name__ == "__main__":
    unittest.main()


