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

    

if __name__ == "__main__":
    unittest.main()