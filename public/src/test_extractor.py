#!/usr/bin/env python3
import unittest
from blocksplitter import *
from textnode import *

class test_extractor(unittest.TestCase):
    def test_firstExtractor(self):
        old_node = (TextNode("This is test text with a ![funny image](www.google.com) and a potential link to a ![troll image](www.troll.com)",TextType.NORMAL))
        functionRun = split_nodes_image([old_node])
        expectedOutcome = [
            TextNode("This is test text with a ", TextType.NORMAL),
            TextNode("funny image", TextType.IMAGES, "www.google.com"),
            TextNode(" and a potential link to a ", TextType.NORMAL),
            TextNode("troll image", TextType.IMAGES, "www.troll.com")
        ]
        self.assertEqual(functionRun, expectedOutcome)
    def test_firstLinkExtractor(self):
        old_node = (TextNode("This is a funny test with a link [to the moon](www.themoon.com) and hopefully it returns successfully", TextType.NORMAL))
        functionRun = split_nodes_link([old_node])
        expectedOutcome = [
            TextNode("This is a funny test with a link ", TextType.NORMAL),
            TextNode("to the moon", TextType.LINKS, "www.themoon.com"),
            TextNode(" and hopefully it returns successfully", TextType.NORMAL)
        ]
        self.assertEqual(functionRun, expectedOutcome)
    def test_secondExtractor(self):
        old_node = TextNode("Here is an image ![funny cat](www.cat.com) and another ![happy dog](www.dog.com)", TextType.NORMAL)
        functionRun = split_nodes_image([old_node])
        expectedOutcome = [
            TextNode("Here is an image ", TextType.NORMAL),
            TextNode("funny cat", TextType.IMAGES, "www.cat.com"),
            TextNode(" and another ", TextType.NORMAL),
            TextNode("happy dog", TextType.IMAGES, "www.dog.com")
        ]
        self.assertEqual(functionRun, expectedOutcome)

    def test_secondLinkExtractor(self):
        old_node = TextNode("This is a test with [a link](www.test.com) and another [link](www.example.com)", TextType.NORMAL)
        functionRun = split_nodes_link([old_node])
        expectedOutcome = [
            TextNode("This is a test with ", TextType.NORMAL),
            TextNode("a link", TextType.LINKS, "www.test.com"),
            TextNode(" and another ", TextType.NORMAL),
            TextNode("link", TextType.LINKS, "www.example.com")
        ]
        self.assertEqual(functionRun, expectedOutcome)

    def test_emptyExtractor(self):
        old_node = TextNode("This has no images or links.", TextType.NORMAL)
        functionRun = split_nodes_image([old_node])
        expectedOutcome = [TextNode("This has no images or links.", TextType.NORMAL)]
        self.assertEqual(functionRun, "No images in text")

    def test_onlyLinks(self):
        old_node = TextNode("Link [one](www.one.com) and [two](www.two.com)", TextType.NORMAL)
        functionRun = split_nodes_link([old_node])
        expectedOutcome = [
            TextNode("Link ", TextType.NORMAL),
            TextNode("one", TextType.LINKS, "www.one.com"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("two", TextType.LINKS, "www.two.com")
        ]
        self.assertEqual(functionRun, expectedOutcome)

    def test_onlyImages(self):
        old_node = TextNode("![image1](www.img1.com) and ![image2](www.img2.com)", TextType.NORMAL)
        functionRun = split_nodes_image([old_node])
        expectedOutcome = [
            TextNode("image1", TextType.IMAGES, "www.img1.com"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("image2", TextType.IMAGES, "www.img2.com")
        ]
        self.assertEqual(functionRun, expectedOutcome)

    def test_noBrackets(self):
        old_node = TextNode("This text has no brackets or links.", TextType.NORMAL)
        functionRun = split_nodes_link([old_node])
        expectedOutcome = "No links in text"
        self.assertEqual(functionRun, expectedOutcome)


if __name__ == "__main__":
    unittest.main()