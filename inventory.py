
inventory = [
   {"item_1": {
       "name": "Rolls Roys Droptail",
       "id": "RRD2024",
       "stock": 3,
       "price": 37000000
   }
    },
   {"item_2": {
       "name": "Pagani Zonda HP Barchetta",
       "id": "PZB 2024",
       "stock": 7,
       "price": 15000000
   }
    },
   {"item_3": {
       "name": "Bugatti Chironnn Profilée",
       "id": "BCP23",
       "stock": 4,
       "price": 12000000
   }
    },
   {"item_4": {
       "name": "Maybach Exelero (2004)",
       "id": "MX2004",
       "stock": 8,
       "price": 9000000
   }
    },
   {"item_5": {
       "name": "Koenigsegg Jesko Attack",
       "id": "KJA",
       "stock": 5,
       "price": 3700000
   }
    }
]

# view all items

print(f"item_1:\n  Name: {inventory[0]['item_1']['name']}\n  ID: {inventory[0]['item_1']['id']}\n  Stock: {inventory[0]['item_1']['stock']}\n  Price: ${inventory[0]['item_1']['price']:,}\n\n")

print(f"item_2:\n  Name: {inventory[1]['item_2']['name']}\n  ID: {inventory[1]['item_2']['id']}\n  Stock: {inventory[1]['item_2']['stock']}\n  Price: ${inventory[1]['item_2']['price']:,}\n")

print(f"item_3:\n  Name: {inventory[2]['item_3']['name']}\n  ID: {inventory[2]['item_3']['id']}\n  Stock: {inventory[2]['item_3']['stock']}\n  Price: ${inventory[2]['item_3']['price']:,} \n")

print(f"item_4:\n  Name: {inventory[3]['item_4']['name']}\n  ID: {inventory[3]['item_4']['id']}\n  Stock: {inventory[3]['item_4']['stock']}\n  Price: ${inventory[3]['item_4']['price']:,}\n")

print(f"item_5:\n  Name: {inventory[4]['item_5']['name']}\n  ID: {inventory[4]['item_5']['id']}\n  Stock: {inventory[4]['item_5']['stock']}\n  Price: ${inventory[4]['item_5']['price']:,}\n")


#adding a new item to the existing inventory
inventory.append( {"item_6": {
       "name": "G Wagon",
       "id": "GWG24",
       "stock": 3,
       "price": 200000
   }
    }
)

print(f"item_6:\n Name: {inventory[5]["item_6"]["name"]}\n ID: {inventory[-1]["item_6"]["id"]}\n Stock: {inventory[-1]["item_6"]["stock"]}\n Price: ${inventory[-1]["item_6"]["price"]}\n")

inventory.append( {"item_7": {
       "name": "Mercedes Benz GLE",
       "id": "GLE",
       "stock": 13,
       "price": 270000
   }
    }
)
print(f"item_7:\n Name: {inventory[-1]["item_7"]["name"]}\n ID: {inventory[-1]["item_7"]["id"]}\n Stock: {inventory[-1]["item_7"]["stock"]}\n Price: ${inventory[-1]["item_7"]["price"]}\n")



#updating item 3 stock
inventory[2]["item_3"]["stock"] += 8
print(f"Corrected item_3 stock: {inventory[2]["item_3"]["stock"]}")

#deleting item 5
del inventory[4]
print(f"{inventory}") #no item_5

total_stock_value = 0
for cars in inventory:
    items = list(cars.values())[0]
    total_stock_value += items["stock"] * items["price"]
print(f'Total stock value: ${total_stock_value:,}')