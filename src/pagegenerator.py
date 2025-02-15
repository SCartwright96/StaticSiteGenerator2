from inlineprocessor import *
from htmlnode import *
from blockprocessor import *
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path).read()
    template = open(template_path).read()
    nodes = markdown_to_html_node(markdown)
    html=""
    for node in nodes:
        if len(html)>0:
            html += "\n"
        html+=node.to_html()
    title = extract_title(markdown)

    generated_doc = template.replace("{{ Title }}",title).replace("{{ Content }}", html)
    generate_file_write_paths(dest_path)
    output_doc = open(dest_path, "w")
    output_doc.write(generated_doc)


def generate_file_write_paths(dir):
    file_paths = dir.split("/")
    already_built_path = ""
    for path in file_paths[:-1]:
        if os.path.exists(f"{already_built_path}{path}"):
            already_built_path += f"{path}/"
            continue
        os.mkdir(f"{already_built_path}{path}")
        already_built_path += path

    return already_built_path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = gather_all_files_in_path(dir_path_content)
    for file in files:
        outputpath = file.replace(dir_path_content, dest_dir_path)
        if file.endswith(".md"):
            outputpath = f"{outputpath[:-3]}.html"
            generate_page(file,template_path, outputpath)

def gather_all_files_in_path(path):
    output_files = []
    files_to_collect = os.listdir(path)
    for file in files_to_collect:
        if os.path.isfile(f"{path}{file}"):
            output_files.append(f"{path}{file}")
            continue
        output_files.extend(gather_all_files_in_path(f"{path}{file}/"))
    return output_files