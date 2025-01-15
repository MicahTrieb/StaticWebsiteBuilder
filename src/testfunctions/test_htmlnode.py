#!/usr/bin/env python3  
import unittest

from htmlnode import *


class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        testPropsDict = {
            "prop1":"prop2",
            "prop2":"prop3",
            "prop4":"prop5"

        }
        testOne = HTMLNode("Tag","Value","Children",testPropsDict)
        expectedOutCome = " prop1=prop2 prop2=prop3 prop4=prop5"
        self.assertEqual(testOne.props_to_html(),expectedOutCome)
        
        testTwo = HTMLNode("This will be the tag", "Something something value", "Something children", testPropsDict)
        print(f"This is the tag: {testTwo.tag}\nThis is the value: {testTwo.value}\nThis is the children: {testTwo.children}\nThis is the props: {testTwo.props}\nThis is the props converted:",testTwo.props_to_html())
              
              


if __name__ == "__main__":
    unittest.main()

