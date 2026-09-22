class Publication:

    def __init__(self, name):
        self.name = name

class Book(Publication):

    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book Name: {self.name}\nAuthor: {self.author}\nPages: {self.pages}\n")
        
class Magazine(Publication):

    def __init__(self, name, chief):
        super().__init__(name)
        self.chief = chief

    def print_information(self):
        print(f"Magazine Name: {self.name}\nChief Editor: {self.chief}\n")

meow = Book("Compartment No. 6", "Rosa Liksom", 192)
meow.print_information()

woof = Magazine("Donald Duck", "Aki Hyyppä")
woof.print_information()
