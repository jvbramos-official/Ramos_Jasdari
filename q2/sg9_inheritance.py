class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    #property is used to get the title
    @property
    def title(self):
        return self.__title

    #property is used to get the author
    @property
    def author(self):
        return self.__author
   #sets title and allows change     
    @title.setter
    def title(self, title):
        self.__title = title
    #sets author and allows change
    @author.setter
    def author (self, author):
        self.__author = author
    #displays info into a neat and organized place    
    def display_info(self):
        print(f"\nTitle: {self.__title}")
        print(f"Author: {self.__author}")
#creates child class Book        
class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages
        
    @property
    def number_of_pages(self):
        return self.__number_of_pages
        
    @number_of_pages.setter
    def number_of_pages(self, pages):
        #checks whether new page is 0
        if pages >= 0:
            self.__number_of_pages = pages
        else:
            self.__number_of_pages = None
            
    #displays info into a neat and organized place        
    def display_info(self):
        super().display_info()
        #checks whether the new page is 0 and returns the number
        if self.__number_of_pages is not None:
            print(f"Number of pages: {self.__number_of_pages}")
        else:
            print("The Number of pages must be positive.")
#creates child class Magazine            
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
    
    @property
    def issue_number(self):
            return self.__issue_number
        
    @issue_number.setter
    def issue_number(self, number):
        #checks whether new issue number is 0
        if number >= 0:
            self.__issue_number = number
        else:
           self.__issue_number = None
    #displays info into a neat and organized place        
    def display_info(self):
        super().display_info()
        #checks whether the new issue number is 0 and returns the number
        if self.__issue_number is not None:
            print(f"Issue Number: {self.__issue_number}")
        else:
            ("The Issue number must be positive.")
        
print("Publication Information:")
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub1.display_info()

pub2 = Publication("Simon the Narcisist", "Jasdari Ramos\n")
pub2.display_info()

print("Book Information:")
book1 = Book("The Hobbit", "J.R.R. Tolkien", -310)
book1.display_info()

book2 = Book("Miss ko na siya", "Reyne Leanne", 676)
book2.display_info()

print("\nMagazine Information:")
mag1 = Magazine("National Geographic", "Various Authors", 202)
mag1.display_info()

mag2 = Magazine("\nGusto ko Money", "Claire Olano", 100)
mag2.display_info()
