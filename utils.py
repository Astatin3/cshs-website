from bottle import route, run, static_file, redirect

root = "./static/"
root_img = root+"img/"
root_js = root+"js/"

# Only calculate page content once, and return a way to access it
def page(name, elements):
    value = add_elements(load_file("pages/"+name+".html"), elements)
    return lambda: value

# Only calculate page content once, and return a way to access it
def page_error(name, elements):
    value = add_elements(load_file("pages/"+name+".html"), elements)
    return lambda e: value

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
        element = add_elements(load_file(value), elements)
        source = source.replace(replace_str, element)
    return source
