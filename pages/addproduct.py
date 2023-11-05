
from taipy.gui import Markdown, notify, navigate

from database import insert_one_collection, all_prodcuts
image1 = "https://www.identixweb.com/wp-content/uploads/2022/01/Add-Customization-for-Custom-Products.png"
image2 = "https://img.freepik.com/free-vector/online-wishes-list-concept-illustration_114360-3900.jpg"
name = ""
price = ""
expiry = ""
pid = ""


def submit_action(state):
    if state.pid == "" or state.price == "" or state.expiry == "" or state.pid == "":
        notify(state, 'error', "Product data is invalid")
        return
    product = {
        "pid": int(state.pid),
        "name": state.name,
        "price": state.price,
        "expiry": state.expiry,
        "isavailable": True,
    }

    insert_one_collection(product)
    notify(state, 'info', "Product inserted")
    navigate(state, to="/home")


addproduct_md = Markdown("""
<|toggle|theme|>
<|container|

## Add **Product**{: .color-primary} 📦
 
<|
 <|50 50|layout|class_name= card|
<|
<|layout|columns= 1 1| 
<|
#### Product Id: <|{pid}|input|>
|>
<|
#### Product Name: <|{name}|input|>
|>
|>
 
<br/><br/>
<br/> 
 
 <|
<|layout|columns = 1 1  |
<|
#### Product Price: <|{price}|label=Price|input|>
|>
<|
#### Product Expiry: <|{expiry}|input|>
|>
|>
<br/>
<|submit|button|on_action=submit_action|>
|>
|>
 
<|{image2}|image|height=500px|width=500px|>
|>
|>
 
|> 
       
                  

""")
