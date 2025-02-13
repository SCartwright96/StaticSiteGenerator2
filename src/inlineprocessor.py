from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output_nodes = []
    for old_node in old_nodes:
        new_nodes = []
        if old_node.text_type != TextType.TEXT:
            output_nodes.append(old_node)
            continue
        split_text = old_node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i%2 ==0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_text[i], text_type))
        output_nodes.extend(new_nodes)
    return output_nodes
                



        