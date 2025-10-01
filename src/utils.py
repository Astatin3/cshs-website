from bottle import route, run, static_file, redirect
import markdown

root = "./static/"
root_img = root+"img/"
root_js = root+"js/"
root_css = root+"css/"

# Only calculate page content once, and return a way to access it
def page(name, elements):
    html = add_elements(load_file(name+".html"), elements)
    return lambda: html

# Only calculate page content once, and return a way to access it
def page_error(name, elements):
    html = add_elements(load_file(name+".html"), elements)
    return lambda e: html

# Load the content of a file
def load_file(path: str):
    with open(root+path, "r") as f:
        return f.read()

# Recursively replace the html comment refrences
def add_elements(source: str, elements):
    for key, value in elements.items():
        replace_str = "<!--" + key + "-->"
        if not replace_str in source:
            continue
        element = add_elements(value, elements)
        source = source.replace(replace_str, element)
    return source

# Format text im markdown
def md_format(md_text: str):
    return markdown.markdown(md_text, extensions=["tables", "fenced_code", "codehilite"])

def md_page(name: str, elements: dict):
    elements_clone = elements.copy()
    elements_clone["page"] = md_format(load_file(name+".md"))
    html = md_format(page("pages/markdown_page", elements_clone)())
    return lambda: html