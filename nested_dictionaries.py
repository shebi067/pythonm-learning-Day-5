# # nested dictionary means In one dictionary there is another dictionary
# # for example "A cafe Menu"

# menu = {
#     "burgers": [
#         "Zinger Burger",
#         "Beef Burger",
#         "Grilled Burger"
#     ],
#     "Coffe":[
#         "Espresso",
#         "Americano",
#         "Latte",
#         "Cappichino"
#     ],
#     "Drinks":[
#         "Pepsi",
#         "Coca-Cola",
#         "Marinda"
#     ],
#     "Deserts" :[
#         "Chocolate Lava Cake",
#         "brownie",
#         "Three milk cake"
#     ]
# }

# print(menu["burgers"][2])

# menu["Coffe"].append("Macha")
# # print(menu)

# # loop in differents loop

# for americano, items_list in menu.items():
#     print(f"\n---{americano.upper()} ---")
#     for item in items_list:
#         print("-", item)


tech = {
    "mobile" :{
        "samsung" : "A26",
        "Iphone" : "XS MAx" 
    },
    "Laptop" : {
        "Dell" : "Latitude",
        "Macbook" : "M5 Pro",
        "Lenovo" : "Thinkpad"
    },
    "Power Bank" : {
        "Zero" : "Pro1",
        "Dany" :"Pro 2",
        "Audionic" : "Earbuds",
        "Android" : "Phone"
    }
}
for x in tech:
    print("keys", 2)

           
# print(tech["Power Bank"][-1])

# tech["Laptop"].update("Hp")



