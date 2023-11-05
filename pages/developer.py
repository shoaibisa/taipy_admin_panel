from taipy.gui import Markdown
img1 = "https://www.identixweb.com/wp-content/uploads/2022/01/Add-Customization-for-Custom-Products.png"
developer_md = Markdown("""
<|toggle|theme|>

## Our Team **Mahi**{: .color-primary} 
<|container
<|layout|columns= 1 1 1 |gap=30px|
<|
<|{img1}|image|width=100%|>  
Suruchi
|>
<|
 <|{img1}|image|width=100%|> 
Shoaib
|>
 <|{img1}|image|width=100%|>  
Shivam
|>     
|>                 
""")
