import json
from src.utils import *
from bottle import route


projects_json = "articles.json"

def load_projects():
    json_str = load_file(projects_json)
    return json.loads(json_str)

def format_pages(articles_json: dict, elements: dict):
    for key, value in articles_json.items():
        page_elements = elements.copy()
        page_elements.update({
            "title": value["title"],
            "page": md_format(load_file(value["page"])),
            "image": value["image"]
        })

        page_html = page("elements/article_image", page_elements)() + md_format(load_file(value["page"]))

        page_elements["page"] = page_html

        route("/page/"+key,'GET',  page("pages/markdown_page", page_elements))

def create_article_list(articles_json: dict, elements:dict):
    article_html = ""
    for key, value in articles_json.items():
        page_elements = elements.copy()
        page_elements.update({
            "title": value["title"],
            "subtitle": value["subtitle"],
            # "page": md_format(load_file(value["page"])),
            "image": value["image"],
            "link": "/page/"+key
        })
        article_html += page("elements/article_option", page_elements)()
    return article_html