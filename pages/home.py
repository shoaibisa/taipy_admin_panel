
from taipy.gui import Markdown, notify
from database import all_prodcuts
import pandas

products = all_prodcuts()


del products["_id"]
products["isavailable"].replace({True: "Yes", False: "No"})
yes = 0
no = 0
for i in products["isavailable"]:
    if i == True:
        yes = yes+1
    else:
        no = no+1
data = {
    "Country": ["Sold", "Available"],
    "Area": [yes, no]
}

# for count vs products
# names_count = {}

# for name in products["name"]:
#     if name in names_count:
#         names_count[name] += 1
#     else:
#         names_count = 1

# pairs = []
# for name, count in names_count.items():
#     for i in range(count):
#         pairs.append([name, count])
# data_p_vs_c = pandas.DataFrame(pairs, columns=["Products", "Quantity"])

home_md = Markdown("""
<|toggle|theme|>
<|container|
#  <center>**Rapid~Receipt**{: .color-primary} |Welcome Admin</center>


<|layout|columns=2 1|gap=30px|hover_text=true|
<|
### List of products
                   
<|Table|expandable|
<|{products}|table|width=100%|>
|> 
|>
<|
### Available of Products
<|{data}|chart|type=pie|values=Area|labels=Country|>
|>
|>

### Products sell

 
|>
""")
