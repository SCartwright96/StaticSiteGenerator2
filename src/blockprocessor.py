import re
from htmlnode import *

def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()

    for i in range(len(blocks)-1, 0, -1):
        if len(blocks[i]) == 0:
            blocks.pop(i)
    return blocks

def block_to_blocktype(block):
    if re.search(r"^\#{1,6} .*", block) != None:
        return "heading"
    if re.search(r"^```[\s\S]*```$", block) != None:
        return "code"
    if re.search(r"^>(?:.*\n>)*.*(?!\n)$", block):
        return "quote"
    if re.search(r"^[-*] (?:.*\n[-*] )*.*(?!\n)$", block):
        return "unordered_list"
    
    is_ordered = True
    block_lines = block.split("\n")
    for i in range(1,len(block_lines)+1):
        if block_lines[i-1].startswith(f"{i}. "):
            continue
        else:
            is_ordered = False
            break
    if is_ordered:
        return "ordered_list"

    return "paragraph"

def markdown_to_html_node(markdown):
    output_nodes = []
    blocks = markdown_to_block(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)
        match block_type:
            case "heading":
                head_num = len(re.findall(r"^(#{1,6}) ", block)[0])
                new_text = re.findall(r"^#+ ([\s\S]*)", block)
                output_nodes = LeafNode(f"h{head_num}", new_text[0])
            case "code":
                new_text = re.findall(r"^```([\s\S]*)```$", block)
                output_nodes = ParentNode("pre",LeafNode("code", new_text[0]))

            case "quote":
                text_list = re.findall(r"^>([\s\S]*)$", block, re.M)
                quote_string = ""
                for text in text_list:
                    if len(quote_string)!=0:
                        quote_string += "\n"
                    quote_string += text
                output_nodes = LeafNode("blockquote", quote_string)

            case "unordered_list":
                uo_list = re.findall(r"^[-*] (.*?)$", block, re.M)
                list_nodes = []
                for item in uo_list:
                    list_nodes.append(LeafNode("li", item))
                
                output_nodes = ParentNode("ul", list_nodes)

            case "ordered_list":
                o_list = re.findall(r"^\d+. (.*?)$", block, re.M)
                list_nodes = []
                for item in o_list:
                    list_nodes.append(LeafNode("li", item))
                
                output_nodes = ParentNode("ol", list_nodes)

            case _:
                output_nodes = LeafNode("p", block)
    return output_nodes
