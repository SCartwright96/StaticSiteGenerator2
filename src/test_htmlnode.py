from htmlnode import *
import unittest


class TestHTMLNode(unittest.TestCase):
    def test_propsToHTML(self):
        node = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_not_eq(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p","Test")
        self.assertNotEqual(node,node2)

    def test_eq(self):
        node = HTMLNode("b", "Test")
        node2 = HTMLNode("b", "Test")

        self.assertEqual(node,node2)

    def test_leafNodeNoTag(self):
        node = LeafNode(None,"This is a node with no tag.")
        self.assertEqual("This is a node with no tag.", node.to_html())

    def test_leafNodeWithTag(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leafNodeWithTagAndNoProps(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_ParentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_ParentNodeParentChild(self):
        node = ParentNode(
            "a",
            [
                ParentNode(
                    "b",
                    [LeafNode("c","Top Node")]
                ),
                LeafNode("d", "OuterLeaf")
            ]
        )

        self.assertEqual(node.to_html(), "<a><b><c>Top Node</c></b><d>OuterLeaf</d></a>")

    def test_ParentNodeProps(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"linkText":"Test"}
        )
        self.assertEqual(node.to_html(), "<p linkText=\"Test\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")






if __name__ == "__main__":
    unittest.main()