import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()