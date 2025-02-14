import re

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