import unittest
from inlineprocessor import *

class testInlineProcessor(unittest.TestCase):
    def test_nodedelimiterBold(self):
        node = TextNode("Now **This** is bold text", TextType.TEXT)
        splitnodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertListEqual(splitnodes,
                         [
                             TextNode("Now ",TextType.TEXT),
                             TextNode("This", TextType.BOLD),
                             TextNode(" is bold text", TextType.TEXT)
                         ])
        
    def test_nodedelimiterItalic(self):
        node = TextNode("Now this is *Italic* text", TextType.TEXT)
        splitnodes = split_nodes_delimiter([node],"*",TextType.ITALIC)
        self.assertListEqual(splitnodes,
                         [
                             TextNode("Now this is ",TextType.TEXT),
                             TextNode("Italic", TextType.ITALIC),
                             TextNode(" text", TextType.TEXT)
                         ])
        
    def test_nodedelimiterItalicBoldCode(self):
        node = TextNode("Now **this** **is** *Italic* `text`", TextType.TEXT)
        splitnodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        splitnodes = split_nodes_delimiter(splitnodes,"*",TextType.ITALIC)
        splitnodes = split_nodes_delimiter(splitnodes,"`",TextType.CODE)
        self.assertListEqual(splitnodes,
                         [
                             TextNode("Now ",TextType.TEXT),
                             TextNode("this", TextType.BOLD),
                             TextNode(" ", TextType.TEXT),
                             TextNode("is", TextType.BOLD),
                             TextNode(" ", TextType.TEXT),
                             TextNode("Italic", TextType.ITALIC),
                             TextNode(" ", TextType.TEXT),
                             TextNode("text", TextType.CODE)
                         ])
        
if __name__ == "__main__":
    unittest.main()