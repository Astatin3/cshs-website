from bottle import route, run, static_file, redirect, error
from src.utils import *
from src.projects import *

articles = load_projects()

# Includes other HTML elements inside themselves.
# For example, <!--footer--> in pages will be replaced with the footer source code.
elements = {
    "head": load_file("elements/head.html"),
    "titlebar": load_file("elements/titlebar.html"),
    "footer": load_file("elements/footer.html")
}

# Add list of articles, for article page
elements["articles"] = create_article_list(articles, elements)

format_pages(articles, elements)

# Add redirects to website
# Ex: https://frhs.tech/test -> https://goole.com
route("/github", 'GET', lambda: redirect("https://github.com/astatin3/cshs-website"))


## 
## CSHS
## 

route("/cshs_bylaws", 'GET', lambda: redirect("https://docs.google.com/document/d/1YzR-cGSoa1PBMYJVzNoFG7Nfd5CKWblfK_DRL2tByJ0/edit?usp=sharing"))

# Old, 24-25 route("/masterlog", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1ZhljBt7N1RV-9AyAzdGpuxLDA0Tn9Z7dXlnuojYQzPg/edit?usp=sharing"))
route("/masterlog", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1yVoUb9HwKQ1EzLD8ybuyULA4SckTp8TJ79K-25Yd1Zs/edit?usp=sharing"))
route("/cshs_master_log", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1yVoUb9HwKQ1EzLD8ybuyULA4SckTp8TJ79K-25Yd1Zs/edit?usp=sharing"))


# https://docs.google.com/forms/d/e/1FAIpQLSeVCnBeLAZINfsuv_O8p_GJ2DRyue_IZFRPbi2frTV--aFJJw/viewform
route("/cshs_registration", 'GET', lambda: redirect("https://forms.gle/Gu74zjMJTttQNsLt7"))
route("/cshs_signup", 'GET', lambda: redirect("https://forms.gle/Gu74zjMJTttQNsLt7"))

# Old, 24-25 route("/hourlog", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1RSi9-gsC4HGqME4LLPqivaVEnLsBzDhyhOcCbQalSDs/edit?usp=sharing"))
route("/hourlog", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1FrSHD6S7db_juGQYg3Tou56-KxkRmjMhlmmZfj_8YuQ/edit?usp=sharing"))
route("/cshs_hour_log", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1FrSHD6S7db_juGQYg3Tou56-KxkRmjMhlmmZfj_8YuQ/edit?usp=sharing"))

# Same as mster log
# Old, 24-25 route("/cshs_hour_opps", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1ZhljBt7N1RV-9AyAzdGpuxLDA0Tn9Z7dXlnuojYQzPg/edit?usp=sharing"))
route("/cshs_hour_opps", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1yVoUb9HwKQ1EzLD8ybuyULA4SckTp8TJ79K-25Yd1Zs/edit?usp=sharing"))




route("/instagram", 'GET', lambda: redirect("https://www.instagram.com/fossilridge.cshs/"))

# Route each page to its actual file
route("/", 'GET', page("pages/index", elements))
route("/hackathon", 'GET', page("pages/hackathon", elements))
route("/foodtrucks", 'GET', page("pages/foodtrucks", elements))
route("/board", 'GET', page("pages/board", elements))
route("/codingclub", 'GET', page("pages/codingclub", elements))
route("/cshs", 'GET', page("pages/cshs", elements))
route("/cshs/slides", 'GET', page("pages/cshs_slides", elements))

route("/articles", 'GET', page("pages/articles", elements))
route("/writing_an_article", 'GET', md_page("pages/writing_an_article", elements))

# Route the /img path to the image directory
@route('/img/<filename:path>')
def img(filename):
    return static_file(filename, root=root_img)


# Route the /js path to the javascript directory
@route('/js/<filename:path>')
def js(filename):
    return static_file(filename, root=root_js)

# Route the /css path to the css directory
@route('/css/<filename:path>')
def css(filename):
    return static_file(filename, root=root_css)

error(403, page_error("pages/403", elements))
error(404, page_error("pages/404", elements))

# @error(404)
# def error404(error):
#     return page("404", elements)()

# Run the thing.
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
