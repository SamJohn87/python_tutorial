snacks = ["M&Ms", "Oreo cookies", "Snickers", "Chips", "Granola bars"]

with open("shopping_list.txt", "a") as list_file:
    for snack in snacks:
        list_file.writelines(snack + "\n")


