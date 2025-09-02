from bottle import route, run, static_file, redirect, error
from utils import *

# Includes other HTML elements inside themselves.
# For example, <!--footer--> in pages will be replaced with the footer source code.
elements = {
    "head": "elements/head.html",
    "titlebar": "elements/titlebar.html",
    "footer": "elements/footer.html"
}

# Add redirects to website
# Ex: https://frhs.tech/test -> https://goole.com
route("/github", 'GET', lambda: redirect("https://github.com/emyuan124/cshs-website"))
route("/instagram", 'GET', lambda: redirect("https://www.instagram.com/fossilridge.cshs/"))
route("/msi", 'GET', lambda: redirect("https://docs.google.com/forms/d/1KQjApRs8CiffvLPfwc5be3ujgyJEHAZ1SOLOm1-UD7Q/edit"))
route("/masterlog", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1ZhljBt7N1RV-9AyAzdGpuxLDA0Tn9Z7dXlnuojYQzPg/edit?usp=sharing"))


route("/cshs_bylaws", 'GET', lambda: redirect("https://docs.google.com/document/d/1YzR-cGSoa1PBMYJVzNoFG7Nfd5CKWblfK_DRL2tByJ0/edit?usp=sharing"))
route("/cshs_master_log", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1ZhljBt7N1RV-9AyAzdGpuxLDA0Tn9Z7dXlnuojYQzPg/edit?usp=sharing"))
route("/hourlog", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1RSi9-gsC4HGqME4LLPqivaVEnLsBzDhyhOcCbQalSDs/edit?usp=sharing"))
route("/cshs_hour_log", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1RSi9-gsC4HGqME4LLPqivaVEnLsBzDhyhOcCbQalSDs/edit?usp=sharing"))

# https://docs.google.com/forms/d/e/1FAIpQLSeVCnBeLAZINfsuv_O8p_GJ2DRyue_IZFRPbi2frTV--aFJJw/viewform
route("/cshs_registration", 'GET', lambda: redirect("https://forms.gle/Gu74zjMJTttQNsLt7"))
route("/cshs_signup", 'GET', lambda: redirect("https://forms.gle/Gu74zjMJTttQNsLt7"))
route("/cshs_hour_opps", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1ZhljBt7N1RV-9AyAzdGpuxLDA0Tn9Z7dXlnuojYQzPg/edit?usp=sharing"))



# route("/cshs_signup", 'GET', lambda: redirect("https://docs.google.com/forms/d/e/1FAIpQLSf3AOrpDlTbDzXUyrTfy57vAhtTjYBFyt7pa84ufEldqF4tUw/viewform"))

# route("/aprilsignin", 'GET', lambda: redirect("https://docs.google.com/forms/d/e/1FAIpQLSf75Mtp4tG-ca-spMgnwerskue6YXNKxEguQJei4MpP4JJ_zQ/viewform?usp=sf_link"))
# route("/board-app", 'GET', lambda: redirect("https://docs.google.com/forms/d/e/1FAIpQLScE2OZN9NHb6kfFyqOV8VrNHdL1LH-KYVhrIQSF1QpmaliPSA/viewform?usp=sf_link"))
# route("/challenge", 'GET', lambda: redirect("https://edabit.com/collection/Bz6LEGAhTRwqseZCy"))

# route("/hackathon-exit-2022", 'GET', lambda: redirect("https://docs.google.com/forms/d/e/1FAIpQLSeQVGjTZu8k0mE5CSSzLKl4ZhK0z1CFpzwh_stxKNPHdV1y2w/viewform?usp=pp_url"))
# route("/hackathon-rules-2022", 'GET', lambda: redirect("https://docs.google.com/document/d/1xTA2LrbUGa7YlASj3ZQoFM1UTA4bLj7w3IkrvcgBFsU/edit?usp=sharing"))
# route("/hackathon-rules-scoring-2022", 'GET', lambda: redirect("https://docs.google.com/spreadsheets/d/1L9LBvmYJbjKXM70Wom2uodXDtoosGTmE4dZ2WKLJlXk/edit?usp=sharing"))

# route("/lancom", 'GET', lambda: redirect("https://docs.google.com/forms/d/e/1FAIpQLSetQ8WMLD5o-ak5fKzslC39OrjxxwA-PxzcQ87c-jTGV9IgiA/viewform?usp=sf_link"))
# route("/lipdub", 'GET', lambda: redirect("https://docs.google.com/forms/d/e/1FAIpQLSdUPNbyxhI53ukWtqUli32YmVyF0ffVpPhAln8wE9R7iDKp4A/viewform?usp=sf_link"))
# route("/lp", 'GET', lambda: redirect("https://forms.gle/gTMuib6V2wUVmVn6A"))

# route("/tots", 'GET', lambda: redirect("https://docs.google.com/forms/d/e/1FAIpQLSf3AOrpDlTbDzXUyrTfy57vAhtTjYBFyt7pa84ufEldqF4tUw/viewform"))


# Route each page to its actual file
route("/", 'GET', page("index", elements))
route("/hackathon", 'GET', page("hackathon", elements))
route("/foodtrucks", 'GET', page("foodtrucks", elements))
route("/board", 'GET', page("board", elements))
route("/codingclub", 'GET', page("codingclub", elements))
route("/cshs", 'GET', page("cshs", elements))
route("/cshs/slides", 'GET', page("cshs_slides", elements))

# Route the /img path to the image directory
@route('/img/<filename:path>')
def img(filename):
    return static_file(filename, root=root_img)


# Route the /js path to the javascript directory
@route('/js/<filename:path>')
def js(filename):
    return static_file(filename, root=root_js)

error(403, page_error("403", elements))
error(404, page_error("404", elements))

# @error(404)
# def error404(error):
#     return page("404", elements)()

# Run the thing.
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
