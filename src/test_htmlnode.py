import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        # Test when props is None
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_empty(self):
        # Test when props is an empty dict
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_with_props(self):
        # Test with some props
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props)
        # The order of props in the output may vary, so check for both possibilities
        expected1 = ' href="https://www.google.com" target="_blank"'
        expected2 = ' target="_blank" href="https://www.google.com"'
        result = node.props_to_html()
        self.assertTrue(result == expected1 or result == expected2)

        #LeafNode Tests

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

        #ParentNode Tests

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()