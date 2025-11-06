# class Store:


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

print(myInventory.inventory)
