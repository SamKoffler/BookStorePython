# class Store:
#     def __init__(self, title, author, id):
#         self.title = title
#         self. author = author
#         self.id = id


class Book:
    def __init__(self, title, author, id):
        self.title = title
        self. author = author
        self.id = id
    
    
class Inventory:
    def __init__(self):
        self.inventory = {}
    
    def add_to_inventory(self, book):
        if book.title not in self.inventory:
            self.inventory[book.title] = 1
        else:
            self.inventory[book.title] += 1
        
      
theBible = Book("The Holy Bible", "God", "0001")

warAndPeace = Book("War and Peace", "Leo Tolstoy", "0002")

myInventory = Inventory()

myInventory.add_to_inventory(theBible)
myInventory.add_to_inventory(warAndPeace)

print(myInventory.inventory)
