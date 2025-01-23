#!/usr/bin/env python3
import unittest
from pagegenerator import generate_pages_recursive
import shutil
import os
class RecursiveTest(unittest.TestCase):
    def test_printing_test(self):
        
        startingDirectory = "/home/mici/gitHub/MicahsProjects/staticWebsite/content/"
        TemplateDirectory = "/home/mici/gitHub/MicahsProjects/staticWebsite/template.html"
        targetDirectory = "/home/mici/gitHub/MicahsProjects/staticWebsite/public"
        if os.path.exists(targetDirectory):
            shutil.rmtree(targetDirectory)
        os.mkdir(targetDirectory)
        generate_pages_recursive(startingDirectory, TemplateDirectory, targetDirectory)


if __name__ == "__main__":
    unittest.main()