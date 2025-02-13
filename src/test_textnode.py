import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD,"boot.dev")
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_types(self):
        node = TextNode("This is a text node", TextType.ITALIC,"boot.dev")
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_txNodeToHTMLBold(self):
        node = TextNode("This is now HTML", TextType.BOLD)
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.to_html(), "<b>This is now HTML</b>")

    def test_txNodeToHTMLItalic(self):
        node = TextNode("This is now HTML", TextType.ITALIC)
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.to_html(), "<i>This is now HTML</i>")

    def test_txNodeToHTMLCode(self):
        node = TextNode("This is now HTML", TextType.CODE)
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.to_html(), "<code>This is now HTML</code>")

    def test_txNodeToHTMLLink(self):
        node = TextNode("This is now HTML", TextType.LINK, "google.com")
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.to_html(), "<a href=\"google.com\">This is now HTML</a>")

    def test_txNodeToHTMLImage(self):
        node = TextNode("This is now HTML", TextType.IMAGE, "google.com")
        htmlnode = text_node_to_html_node(node)
        self.assertEqual(htmlnode.to_html(), "<img src=\"google.com\" alt=\"This is now HTML\"></img>")

if __name__ == "__main__":
    unittest.main()