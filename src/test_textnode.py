import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eqtext(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eqtexturl(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD, url=None)
        self.assertEqual(node, node2)
    
    def test_notequrl(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD, "boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_noteqtextnodeurl(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a variable node", TextType.BOLD, "boot.dev")
        self.assertNotEqual(node, node2)
    


    


if __name__ == "__main__":
    unittest.main()
