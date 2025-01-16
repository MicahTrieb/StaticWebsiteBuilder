#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import *
from blocksplitter import *
from extracttitle import extract_title
from directorycopy import *
from pagegenerator import generate_page
from blockmarkdown import *



class TestParentNode(unittest.TestCase):
    #def test_print_directory(self):
        #from_path, template_path, dest_path
    #    generate_page("/home/mici/gitHub/MicahsProjects/staticWebsite/content/index.html","/home/mici/gitHub/MicahsProjects/staticWebsite/template.html","Filler")
    def test_markdown_to_html(self):
        print(markdown_to_html_node('# Tolkien Fan Club\n\n**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn\'t work yet)\n\n> All that is gold does not glitter\n\n## Reasons I like Tolkien\n\n* You can spend years studying the legendarium and still not understand its depths\n* It can be enjoyed by children and adults alike\n* Disney *didn\'t ruin it*\n* It created an entirely new genre of fantasy\n\n## My favorite characters (in order)\n\n1. Gandalf\n2. Bilbo\n3. Sam\n4. Glorfindel\n5. Galadriel\n6. Elrond\n7. Thorin\n8. Sauron\n9. Aragorn\n\nHere\'s what `elflang` looks like (the perfect coding language):\n\n```\nfunc main(){\n    fmt.Println("Hello, World!")\n}\n```\n'))
if __name__ == "__main__":
    unittest.main()


