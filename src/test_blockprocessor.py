import unittest
from blockprocessor import *

class testBlockProcessor(unittest.TestCase):
    def test_markdown_to_blocks(self):
        blocks = markdown_to_block(
"""  # This is a heading

   This is a paragraph of text. It has some **bold** and *italic* words inside of it.

   

   * This is the first list item in a list block
* This is a list item
* This is another list item""")
        self.assertListEqual(blocks,[
"# This is a heading",
"""This is a paragraph of text. It has some **bold** and *italic* words inside of it.""",
"""* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ])

    def test_blocktype_heading1(self):
        testStr = "# This is a big ol wall of text ain't it"
        self.assertEqual(block_to_blocktype(testStr), "heading")

    def test_blocktype_heading2(self):
        testStr = "## This is a big ol wall of text ain't it"
        self.assertEqual(block_to_blocktype(testStr), "heading")

    def test_blocktype_heading3(self):
        testStr = "### This is a big ol wall of text ain't it"
        self.assertEqual(block_to_blocktype(testStr), "heading")

    def test_blocktype_heading4(self):
        testStr = "#### This is a big ol wall of text ain't it"
        self.assertEqual(block_to_blocktype(testStr), "heading")

    def test_blocktype_heading5(self):
        testStr = "##### This is a big ol wall of text ain't it"
        self.assertEqual(block_to_blocktype(testStr), "heading")

    def test_blocktype_heading6(self):
        testStr = "###### This is a big ol wall of text ain't it"
        self.assertEqual(block_to_blocktype(testStr), "heading")

    def test_blocktype_heading7(self):
        testStr = "####### This is a big ol wall of text ain't it"
        self.assertEqual(block_to_blocktype(testStr), "paragraph")

    def test_blocktype_heading_nospace(self):
        testStr = "#This is a big ol wall of text ain't it"
        self.assertEqual(block_to_blocktype(testStr), "paragraph")

    def test_blocktype_code(self):
        testStr =(
"""```This is a block of code. 

It isn't very good```""")
        self.assertEqual(block_to_blocktype(testStr), "code")

    def test_blocktype_code2(self):
        testStr =(
"""```This is a block of code. It isn't very good```""")
        self.assertEqual(block_to_blocktype(testStr), "code")

    def test_blocktype_quote(self):
        testStr =(
""">This is a story
>About A Wall of Test
>That is correct""")
        self.assertEqual(block_to_blocktype(testStr), "quote")

    def test_blocktype_quote2(self):
        testStr =(
""">This is a story
About A Wall of Test
>That is incorrect""")
        self.assertEqual(block_to_blocktype(testStr), "paragraph")
    
    def test_blocktype_shortstory(self):
        testStr =(
""">This is a story""")
        self.assertEqual(block_to_blocktype(testStr), "quote")

    def test_blocktype_unordered(self):
        testStr =(
"""- This is a story
- It is more of a list though
* I hope this works""")
        self.assertEqual(block_to_blocktype(testStr), "unordered_list")

    def test_blocktype_ordered(self):
        testStr =(
"""1. This is a story
2. It is more of a list though
3. I hope this works""")
        self.assertEqual(block_to_blocktype(testStr), "ordered_list")

    def test_blocktype_ordered2(self):
        testStr =(
"""1. This is a story
3. It is more of a list though
3. I hope this works""")
        self.assertEqual(block_to_blocktype(testStr), "paragraph")

    def test_markdown_heading_to_html3(self):
        nodes = markdown_to_html_node("### Heading 3")
        self.assertEqual(nodes[0], LeafNode("h3", "Heading 3"))

    def test_markdown_heading_to_html2(self):
        nodes = markdown_to_html_node("## Heading 2")
        self.assertEqual(nodes[0], LeafNode("h2", "Heading 2"))

    def test_markdown_heading_to_html7(self):
        nodes = markdown_to_html_node("####### Heading 7")
        self.assertEqual(nodes[0], LeafNode("p", "####### Heading 7"))

    def test_markdown_code_to_html(self):
        nodes = markdown_to_html_node("```This is some truly ```awful code``````")
        self.assertEqual(nodes[0], ParentNode("pre",[LeafNode("code", "This is some truly ```awful code```")]))

    def test_markdown_quote_to_html(self):
        nodes = markdown_to_html_node(
            """>This is a test
>of the quote >SYSTEM<""")
        self.assertEqual(nodes[0], LeafNode("blockquote", """This is a test
>of the quote >SYSTEM<"""))
        
    def test_markdown_unordered_list_to_html(self):
        nodes = markdown_to_html_node(
"""* Egg
- Egg 2
* Egg 3"""
        )
        print(nodes)
        self.assertEqual(nodes[0], ParentNode("ul", [
            LeafNode("li","Egg"),
            LeafNode("li","Egg 2"),
            LeafNode("li","Egg 3")
        ]))

    def test_markdown_ordered_list_to_html(self):
        nodes = markdown_to_html_node(
"""1. Egg
2. Egg 2
3. Egg 3"""
        )
        self.assertEqual(nodes[0], ParentNode("ol", [
            LeafNode("li","Egg"),
            LeafNode("li","Egg 2"),
            LeafNode("li","Egg 3")
        ]))

    def test_extract_title(self):
        title = extract_title("""# Let me tell you a story all about how

Paragraph
                          
# Title 2""")
        self.assertEqual(title, "Let me tell you a story all about how")

if __name__ == "__main__":
    unittest.main()