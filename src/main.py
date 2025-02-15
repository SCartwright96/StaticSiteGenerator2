from textnode import *
import os
import shutil
from pagegenerator import *
from staticfilemanager import *

def main():
    shutil.rmtree("public")
    os.mkdir("public")
    replicate_dir("./static/", "./public/") 
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content/", "template.html", "public/")


main()