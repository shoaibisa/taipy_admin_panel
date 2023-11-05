from taipy.gui import Gui, Markdown, navigate
from pages.addproduct import addproduct_md
from pages.home import home_md
from pages.developer import developer_md
favicone = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStQrffFMV3jCG2wB7o7Bs1VwUJ3Z0sWQhbzA&usqp=CAU"

# root_md = "<|menu|label=Menu|lov={[('home', Icon('https://static.vecteezy.com/system/resources/thumbnails/000/616/494/small/home-06.jpg','home')), ('addproduct', 'addproduct')]}|on_action=on_menu|>"


def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)


pages = {
    "/": "<center><|navbar|></center>",
    "home": home_md,
    "addproduct": addproduct_md,
    "team": developer_md,
}


Gui(pages=pages).run(title="Rapid~Receipt", favicon=favicone,
                     run_browser=False, use_reloader=True, port=5555)
