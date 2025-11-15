from src.utils import *

teachers = [
    ["Dannahower", "Mr. Dannahower"],
    ["Menefee", "Mr. Menefee"],
    ["Peardot", "Mr. Peardot"],
    ["Ruffer", "Mr. Ruffer"],
    ["Stone", "Dr. Stone"],
    ["Reimers", "Mr. Reimers"],
    ["Brown", "Mr. Brown"],
    # ["Wilbourn", "Mr. Wilbourn"],
    ["Jackson", "Mr. Jackson"],
]


def beardfy_page(elements):
    b_elements = elements.copy()

    teacher_html = ""

    for teacher in teachers:
        teacher_html += add_elements(
            load_file("elements/beardify_teacher.html"),
            {"img": teacher[0], "name": teacher[1]},
        )

    b_elements.update({"beardify_teacher": teacher_html})

    html = add_elements(load_file("pages/beardify.html"), b_elements)
    # print(html)
    return lambda: html
