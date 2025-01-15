#!/usr/bin/env python3
import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_basic_leaf_node(self):
        # Test a basic leaf node with tag, value, and no props
        leaf = LeafNode(tag="p", value="Hello, world!")
        expected_output = "<p>Hello, world!</p>"
        self.assertEqual(leaf.to_html(), expected_output)

    def test_leaf_node_with_props(self):
        # Test a leaf node with tag, value, and props
        leaf = LeafNode(tag="span", value="Styled text", props={"class": "highlight", "id": "text1"})
        expected_output = '<span class="highlight" id="text1">Styled text</span>'
        self.assertEqual(leaf.to_html(), expected_output)

    def test_leaf_node_no_tag(self):
        # Test a leaf node with no tag (just the value)
        leaf = LeafNode(value="Plain text")
        expected_output = "Plain text"
        self.assertEqual(leaf.to_html(), expected_output)

    def test_leaf_node_no_value(self):
        # Test a leaf node with no value, expecting a ValueError
        leaf = LeafNode(tag="div", props={"class": "empty"})
        with self.assertRaises(ValueError):
            leaf.to_html()

    def test_leaf_node_empty_props(self):
        # Test a leaf node with tag, value, and empty props
        leaf = LeafNode(tag="h1", value="Title", props={})
        expected_output = "<h1>Title</h1>"
        self.assertEqual(leaf.to_html(), expected_output)
    def test_special_characters_in_value(self):
        leaf = LeafNode(tag="h1", value="@&^!@#&!TEST", props={2:3})
        expected_output = '<h1 2="3">@&^!@#&!TEST</h1>'
        self.assertEqual(leaf.to_html(),expected_output)
    def test_empty_value_string(self):
        leaf = LeafNode(tag="a", value="")
        self.assertEqual(leaf.to_html(),"<a></a>")
    def test_special_characters_in_props(self):
        leaf = LeafNode(tag="a", value="We're testing this huh...",props={"$":3,"#":4})
        expected_output = '<a $="3" #="4">We\'re testing this huh...</a>'
        self.assertEqual(leaf.to_html(),expected_output)
    def test_escaping_text(self):
        leaf = LeafNode(tag="p", value="a < b && c > d")
        expected_output = '<p>a < b && c > d</p>'
        self.assertEqual(leaf.to_html(),expected_output)
    def test_spaces_or_quotes(self):
        leaf = LeafNode(tag="a", value="click", props={"title": "my special link"})
        expected_output = '<a title="my special link">click</a>'
        self.assertEqual(leaf.to_html(),expected_output)
if __name__ == "__main__":
    unittest.main()
