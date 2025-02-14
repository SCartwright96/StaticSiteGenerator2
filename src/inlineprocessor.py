from textnode import *
import re

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

def split_nodes_image(old_nodes):
    output_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            output_nodes.append(old_node)
            continue
        images_tuples = extract_markdown_images(old_node.text)
        if len(images_tuples) == 0:
            output_nodes.append(old_node)
            continue
        
        remaining_text = old_node.text
        for i in range(len(images_tuples)):
            split_text=remaining_text.split(f"![{images_tuples[i][0]}]({images_tuples[i][1]})", 1)
            if len(split_text[0]) != 0:
                output_nodes.append(TextNode(split_text[0], TextType.TEXT))
            output_nodes.append(TextNode(images_tuples[i][0], TextType.IMAGE, images_tuples[i][1]))
            if len(split_text) == 1:
                 remaining_text = ""
            else:
                remaining_text=split_text[1]
        if len(remaining_text) > 0:
            output_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return output_nodes
                
def split_nodes_link(old_nodes):
    output_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            output_nodes.append(old_node)
            continue
        link_tuples = extract_markdown_links(old_node.text)
        if len(link_tuples) == 0:
            output_nodes.append(old_node)
            continue
        
        remaining_text = old_node.text
        for i in range(len(link_tuples)):
            split_text=remaining_text.split(f"[{link_tuples[i][0]}]({link_tuples[i][1]})", 1)
            if len(split_text[0]) != 0:
                output_nodes.append(TextNode(split_text[0], TextType.TEXT))
            output_nodes.append(TextNode(link_tuples[i][0], TextType.LINK, link_tuples[i][1]))
            if len(split_text) == 1:
                 remaining_text = ""
            else:
                remaining_text=split_text[1]
        if len(remaining_text) > 0:
            output_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return output_nodes

def extract_markdown_images(text):
    Images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return Images

def extract_markdown_links(text):
    Images = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return Images

def text_to_textnodes(text):
    nodes = [TextNode(text,TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*",TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`",TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes