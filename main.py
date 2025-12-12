# class Store:


class Item:
    def __init__(self, itemName, id):
        self.itemName = itemName
        self.id = id

class Book(Item):
    def __init__(self, title, author, id):
        self.title = title
        self.author = author
        self.id = id

class Magazine(Item):
    def __init__(self, name, issue, id):
        self.name = name
        self.issue = issue
        self.id = id

class DVD(Item):
    def __init__(self, title, runtime, id):
        self.title = title
        self.runtime = runtime
        self.id = id
    
    
class Inventory:
    def __init__(self):
        self.inventory = {}
    
    def add_to_inventory(self, item):
        if item.id not in self.inventory:
            self.inventory[item.id] = 1
        else:
            self.inventory[item.id] += 1
            

theBible = Book("The Holy Bible", "God", "0001")
warAndPeace = Book("War and Peace", "Leo Tolstoy", "0002")
mobyDick = Book("Moby Dick", "Herman Melville", "0003")
prideAndPrejudice = Book("Pride and Prejudice", "Jane Austen", "0004")
greatGatsby = Book("The Great Gatsby", "F. Scott Fitzgerald", "0005")
nineteenEightyFour = Book("1984", "George Orwell", "0006")
toKillAMockingbird = Book("To Kill a Mockingbird", "Harper Lee", "0007")
ulysses = Book("Ulysses", "James Joyce", "0008")
catcherInTheRye = Book("The Catcher in the Rye", "J.D. Salinger", "0009")
hobbit = Book("The Hobbit", "J.R.R. Tolkien", "0010")
odyssey = Book("The Odyssey", "Homer", "0011")
divineComedy = Book("The Divine Comedy", "Dante Alighieri", "0012")

bagel = Item("Bagel", "0013")
timeMagazine = Magazine("TIME", "January 2025", "0014")
theMatrix = DVD("The Matrix", "136 minutes", "0015")

myInventory = Inventory()

myInventory.add_to_inventory(theBible)
myInventory.add_to_inventory(theBible)
myInventory.add_to_inventory(warAndPeace)
myInventory.add_to_inventory(mobyDick)
myInventory.add_to_inventory(mobyDick)
myInventory.add_to_inventory(mobyDick)
myInventory.add_to_inventory(prideAndPrejudice)
myInventory.add_to_inventory(greatGatsby)
myInventory.add_to_inventory(nineteenEightyFour)
myInventory.add_to_inventory(toKillAMockingbird)
myInventory.add_to_inventory(ulysses)
myInventory.add_to_inventory(catcherInTheRye)
myInventory.add_to_inventory(hobbit)
myInventory.add_to_inventory(odyssey)
myInventory.add_to_inventory(divineComedy)
myInventory.add_to_inventory(divineComedy)

myInventory.add_to_inventory(bagel)
myInventory.add_to_inventory(timeMagazine)
myInventory.add_to_inventory(theMatrix)

print(myInventory.inventory)
