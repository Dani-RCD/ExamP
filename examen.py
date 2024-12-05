class User:
    def __init__(self, name):
        self.__name = name  # Encapsulamiento del nombre User

    @property
    def name(self):
        return self.__name
#Busca y seleciona el libro
    def search_book(self, book_name):
        print(f"{self.name} is searching for the book: {book_name}") 
    def select_book(self, book_name):
        print(f"{self.name} selected the book: {book_name}") 

#Lista de libros en el catalogo
class Catalogue:
    def __init__(self):
        self.__books = []  # Encapsulamiento del catalogo. 

    def add_book(self, book_name):
        self.__books.append(book_name)
        print(f"Book '{book_name}' added to the catalogue.") #Agrega

    def check_available_books(self):
        print("Available books in the catalogue:") #Disponibilidad del libro
        for book in self.__books:
            print(f"- {book}")


class AvailableBooks(Catalogue):  # Herencia de la clase
    def __init__(self):
        super().__init__()

    def check_availability(self, book_name):
        if book_name in self._Catalogue__books:  # Acceso a atributos heredados
            print(f"The book '{book_name}' is available.")
            return True
        else:
            print(f"The book '{book_name}' is not available.")
            return False


class Loan:
    def __init__(self):
        self.__loans = []  # Encapsulamiento

    def borrow_book(self, user, book_name, available_books):
        try:  # Manejo de errores
            if available_books.check_availability(book_name):
                self.__loans.append({"user": user.name, "book": book_name})
                available_books._Catalogue__books.remove(book_name)  # Acceso a atributo privado
                print(f"{user.name} has borrowed the book: {book_name}")
            else:
                raise ValueError(f"{book_name} is not available.")
        except ValueError as e:
            print(e)

    def return_book(self, user, book_name, available_books):
        for loan in self.__loans:
            if loan["user"] == user.name and loan["book"] == book_name:
                self.__loans.remove(loan)
                available_books.add_book(book_name)
                print(f"{user.name} has returned the book: {book_name}")
                return
        print(f"No record found for {user.name} borrowing {book_name}.")

    def check_penalties(self, user):
        print(f"Checking penalties for {user.name}...")
        # Placeholder for penalty logic
        print("No penalties found.")


# Polimorfismo: Ejemplo
class PremiumUser(User):
    def search_book(self, book_name):
        print(f"{self.name} (Premium User) is searching for the book: {book_name}")


# Menu System
if __name__ == "__main__":
    catalogue = Catalogue()
    available_books = AvailableBooks()
    loan_system = Loan()

    while True:
        print("\n--- Library System Menu ---")
        print("1. Add a book to the catalogue")
        print("2. View available books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Check penalties")
        print("6. Exit")

        try:
            choice = int(input("Select an option: "))

            if choice == 1:
                book_name = input("Enter the book name to add: ")
                catalogue.add_book(book_name)
                available_books.add_book(book_name)

            elif choice == 2:
                catalogue.check_available_books()

            elif choice == 3:
                user_name = input("Enter your name: ")
                user = User(user_name)
                book_name = input("Enter the book name to borrow: ")
                loan_system.borrow_book(user, book_name, available_books)

            elif choice == 4:
                user_name = input("Enter your name: ")
                user = User(user_name)
                book_name = input("Enter the book name to return: ")
                loan_system.return_book(user, book_name, available_books)

            elif choice == 5:
                user_name = input("Enter your name: ")
                user = User(user_name)
                loan_system.check_penalties(user)

            elif choice == 6:
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Please enter a valid number.")
