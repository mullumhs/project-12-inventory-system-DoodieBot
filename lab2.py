"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item




# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.

class inventory_manager:
    def __init__(self):
        self._item=[]



# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

def add_item(self, item):
    for exist_item in self.items:
        if exist_item.get_name() == item.get_name():
            return False
    self.item.append(item)
    return True


def remove_item(self, item):
    for exist_item in self.items:
        if exist_item.get_name() == item.get_name():
            self.item.remove
            return False

