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
        
    def test_extract_markdown_images(self):
        images = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(images,[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
    def test_extract_markdown_links(self):
        links = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
        
    def test_extract_markdown_link_avoid_image(self):
        images = extract_markdown_links("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(images,[("rick roll", "https://i.imgur.com/aKaOqIh.gif")])

    def test_extract_markdown_image_avoid_link(self):
        images = extract_markdown_images("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(images,[("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT)
        nodes = split_nodes_image([node])
        self.assertListEqual(nodes,[
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ])

    def test_split_nodes_images_ignore_link(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT)
        nodes = split_nodes_image([node])
        self.assertListEqual(nodes,[
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT),
        ])

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT)
        nodes = split_nodes_link([node])
        self.assertListEqual(nodes,[
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ])

    def test_split_nodes_link_and_image(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT)
        nodes = split_nodes_image([node])
        nodes = split_nodes_link(nodes)
        self.assertListEqual(nodes,[
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ])

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])


if __name__ == "__main__":
    unittest.main()