# library class

class Library:
    
    def __init__(self,list_of_book,library_name):

        self.list_of_book = list_of_book
        self.library_name = library_name
        self.lend_dict ={}   # dictionary

        print(f"####### Welcome To The {self.library_name} #########")


    def display_book(self):
        print(f"####### We have the following books in our Library  {self.library_name}######")
        for book in self.list_of_book:
            print(book)

    def lend_book(self,user_name,book_name):
        print("########## lend book #####")

        self.user_name = user_name
        self.book_name = book_name
        
        if book_name in self.list_of_book:
            print("##### Book is available")

            if book_name not in self.lend_dict.keys():
                self.lend_dict.update({book_name:user_name})
                print("Lender-Bool database has been updated")

            else:
                print(f"This Book is alreday taken by {self.lend_dict[book_name]}")   
     
        else:
            print("Book is not available")

    def add_book(self,addbook):
        print("####### Add Book ########")
        self.addbook = addbook
        self.list_of_book.append(self.addbook)
        self.display_book() # calling methods


    def return_book(self,return_book):
        print("####### return book ######")
        self.return_book = return_book
        
        if self.return_book in self.list_of_book:
            
            self.lend_dict.pop(self.return_book)
            print("Thanks for returning the book")

        else:
            print("This book is not issued from this library")   


def main_fxn():
    #creating object of class
    obj1 = Library(["hindi","punjabi","English"],"Central Library")

    k = True
    while (k is not False) :

        user_choice = input("Option  display, lend, add, return : ")


        if user_choice == "display":
            obj1.display_book()

        elif user_choice == "lend": 
            user_name = input("Please Enter Your Name : ")   
            book_name = input("Please Enter the Name of book Which do you wanna lend : ")
            obj1.lend_book(user_name,book_name)

        elif user_choice == "add":    
            addbook = input("Please Enter name of New book :")
            obj1.add_book(addbook)

        elif user_choice == "return" :   
            return_book = input("Please Enter the name of book do wana to return : ")
            obj1.return_book(return_book)

        k = input("Continue (yes /no) :")
        if k == 'no':
            k = False
        else :
            k = True    

if __name__ == "__main__":
    main_fxn()

# If file is not imported