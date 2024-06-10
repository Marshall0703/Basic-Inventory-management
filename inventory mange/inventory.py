import tkinter as tk

def add_inventory():
    item_name = item_name_entry.get()
    item_qty = item_qty_entry.get()
    with open('inventory.txt', 'a') as file:
        file.write(f'{item_name},{item_qty}\n')
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)

def update_inventory():
    item_name = item_name_entry.get()
    item_qty = item_qty_entry.get()
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    with open('inventory.txt', 'w') as file:
        for line in inventory_data:
          name, qty = line.strip().split(',')
          if name == item_name:
            file.write(f'{name},{item_qty}\n')
          else:
            file.write(line)
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)

def search_inventory():
    search_name = item_name_entry.get()
    with open('inventory.txt', 'r') as file:
        for line in file:
            name, qty = line.strip().split(',')
            if name == search_name:
                result_label.config(text = f'{name} - {qty}')
                return
    result_label.config(text = f'{search_name} not found.')
    item_name_entry.delete(0, tk.END)

def remove_inventory():
    remove_name = item_name_entry.get()
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    with open('inventory.txt', 'w') as file:
        for line in inventory_data:
            name, qty = line.strip().split(',')
            if name != remove_name:
                file.write(line)
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)

def generate_inventory():
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    inventory_text = ''.join(inventory_data)
    result_label.config(text = inventory_text)

root = tk.Tk()
root.title("Basic Management")

item_name_label = tk.Label(root, text = "Item Name:")
item_name_entry = tk.Entry(root)
item_qty_label = tk.Label(root, text = "Item QTY:")
item_qty_entry = tk.Entry(root)
item_name_label.grid(row = 0, column = 0, padx = 5, pady = 5)
item_name_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
item_qty_label.grid(row = 1, column = 0, padx = 5, pady = 5)
item_qty_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

add_button = tk.Button(root, text = "Add Inventory", command = add_inventory)
update_button = tk.Button(root, text = "Update Inventory", command = update_inventory)
search_button = tk.Button(root, text = "Search Inventory", command = search_inventory)
remove_button = tk.Button(root, text = "Remove Inventory", command = remove_inventory)
generate_button = tk.Button(root, text = "Load Inventory", command = generate_inventory)
result_label = tk.Label(root, text = "List")

add_button.grid(row = 2, column = 0, padx = 5, pady = 5)
update_button.grid(row = 2, column = 1, padx = 5, pady = 5)
search_button.grid(row = 3, column = 0, padx = 5, pady = 5)
remove_button.grid(row = 3, column = 1, padx = 5, pady = 5)
generate_button.grid(row = 4, column = 0, padx = 5, pady = 5)
result_label.grid(row = 5, column = 0, padx = 5, pady = 5)

root.mainloop()