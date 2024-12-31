#!/usr/bin/env python3
import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_basic_parent_node(self):
        # ParentNode with one child
        child = LeafNode(tag="p", value="Child content")
        parent = ParentNode(tag="div", children=[child], props=None)
        self.assertEqual(parent.to_html(), "<div><p>Child content</p></div>")

    def test_multiple_children(self):
        # ParentNode with multiple children
        child1 = LeafNode(tag="p", value="Child 1")
        child2 = LeafNode(tag="span", value="Child 2")
        parent = ParentNode(tag="div", children=[child1, child2])
        self.assertEqual(parent.to_html(), "<div><p>Child 1</p><span>Child 2</span></div>")

    def test_nested_parent_node(self):
        # ParentNode with nested ParentNode
        child = LeafNode(tag="p", value="Nested child")
        nested = ParentNode(tag="section", children=[child])
        parent = ParentNode(tag="div", children=[nested])
        self.assertEqual(parent.to_html(), "<div><section><p>Nested child</p></section></div>")

''    def test_no_children(self):
        # ParentNode without children
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=[]).to_html()

    def test_none_children(self):
        # ParentNode with None as children
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=None).to_html()

    def test_empty_tag(self):
        # ParentNode with an empty tag
        child = LeafNode(tag="p", value="Child")
        with self.assertRaises(ValueError):
            ParentNode(tag="", children=[child]).to_html()

    def test_none_tag(self):
        # ParentNode with None as a tag
        child = LeafNode(tag="p", value="Child")
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[child]).to_html()

    def test_non_string_tag(self):
        # ParentNode with a non-string tag
        child = LeafNode(tag="p", value="Child")
        with self.assertRaises(ValueError):
            ParentNode(tag=123, children=[child]).to_html()

    def test_special_character_tag(self):
        # ParentNode with special character tag
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="div-123", children=[child])
        self.assertEqual(parent.to_html(), "<div-123><p>Child</p></div-123>")

    def test_props_in_parent_node(self):
        # ParentNode with properties
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="section", children=[child], props={"class": "container"})
        self.assertEqual(parent.to_html(), '<section class="container"><p>Child</p></section>')

    def test_empty_props(self):
        # ParentNode with empty properties
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="section", children=[child], props={})
        self.assertEqual(parent.to_html(), "<section><p>Child</p></section>")

    def test_props_with_symbols(self):
        # ParentNode with properties containing symbols
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="section", children=[child], props={"data-info": "123&456"})
        self.assertEqual(parent.to_html(), '<section data-info="123&456"><p>Child</p></section>')

    def test_props_with_spaces(self):
        # ParentNode with properties containing spaces
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="section", children=[child], props={"class": "main container"})
        self.assertEqual(parent.to_html(), '<section class="main container"><p>Child</p></section>')

    def test_mixed_children(self):
        # ParentNode with mixed children (LeafNode and ParentNode)
        child1 = LeafNode(tag="p", value="Text")
        child2 = ParentNode(tag="div", children=[LeafNode(tag="span", value="Nested")])
        parent = ParentNode(tag="section", children=[child1, child2])
        self.assertEqual(parent.to_html(), "<section><p>Text</p><div><span>Nested</span></div></section>")

    def test_invalid_children(self):
        # ParentNode with invalid children type
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children="not_a_list").to_html()

    def test_invalid_child_node(self):
        # ParentNode with an invalid child
        with self.assertRaises(AttributeError):
            ParentNode(tag="div", children=["invalid_child"]).to_html()

    def test_empty_children_list(self):
        # ParentNode with an empty children list
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=[]).to_html()

    def test_non_dict_props(self):
        # ParentNode with non-dictionary props
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="section", children=[child], props="invalid_props")
        self.assertEqual(parent.to_html(), "<section><p>Child</p></section>")

    def test_none_props(self):
        # ParentNode with None props
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="section", children=[child], props=None)
        self.assertEqual(parent.to_html(), "<section><p>Child</p></section>")

    def test_unicode_tag(self):
        # ParentNode with a unicode tag
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="div-测试", children=[child])
        self.assertEqual(parent.to_html(), "<div-测试><p>Child</p></div-测试>")

    def test_unicode_props(self):
        # ParentNode with unicode in props
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="div", children=[child], props={"data-test": "测试"})
        self.assertEqual(parent.to_html(), '<div data-test="测试"><p>Child</p></div>')

    def test_unicode_children(self):
        # ParentNode with unicode child values
        child = LeafNode(tag="p", value="内容")
        parent = ParentNode(tag="div", children=[child])
        self.assertEqual(parent.to_html(), "<div><p>内容</p></div>")

    def test_missing_props(self):
        # ParentNode with missing props argument
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="section", children=[child])
        self.assertEqual(parent.to_html(), "<section><p>Child</p></section>")

    def test_large_children_list(self):
        # ParentNode with a large number of children
        children = [LeafNode(tag="p", value=f"Child {i}") for i in range(100)]
        parent = ParentNode(tag="div", children=children)
        html_output = parent.to_html()
        self.assertTrue(html_output.startswith("<div>") and html_output.endswith("</div>"))

    def test_whitespace_tag(self):
        # ParentNode with whitespace tag
        child = LeafNode(tag="p", value="Child")
        with self.assertRaises(ValueError):
            ParentNode(tag="   ", children=[child]).to_html()''

    def test_special_character_props(self):
        # ParentNode with special characters in props
        child = LeafNode(tag="p", value="Child")
        parent = ParentNode(tag="div", children=[child], props={"data-info": "value with spaces"})
        self.assertEqual(parent.to_html(), '<div data-info="value with spaces"><p>Child</p></div>')

    def test_malformed_children(self):
        # ParentNode with malformed children objects
        child = object()  # Not a valid HTMLNode
        with self.assertRaises(AttributeError):
            ParentNode(tag="div", children=[child]).to_html()

    def test_self_closing_children(self):
        # ParentNode with self-closing children
        child = LeafNode(tag="img", value="")
        parent = ParentNode(tag="div", children=[child])
        self.assertEqual(parent.to_html(), "<div><img></img></div>")

    def test_empty_props_and_children(self):
        # ParentNode with empty props and no children
        with self.assertRaises(ValueError):
            ParentNode(tag="div", props={}, children=[]).to_html()


if __name__ == "__main__":
    unittest.main()
