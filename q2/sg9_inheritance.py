class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        
    @property
    def title(self):
        return self.__title
        
    @property
    def author(self):
        return self.__author
        
    @title.setter
    def title(self, title):
        self.__title = title
    
    @author.setter
    def author (self, author):
        self.__author = author
        
    def display_info(self):
        print(f"\nTitle: {self.__title}")
        print(f"Author: {self.__author}")
        
class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages
        
    @property
    def number_of_pages(self):
        return self.__number_of_pages
        
    @number_of_pages.setter
    def number_of_pages(self, number_of_pages):
        if number_of_pages >= 0:
            self.__number_of_pages = number_of_pages
        else:
            return "The number of pages must be positive"
            
    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.__number_of_pages}")
            
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number
    
    @property
    def issue_number(self):
        return self.issue_number
        
    @issue_number.setter
    def issue_number(self, issue_number):
        if issue_number >= 0:
            self.issue_number = issue_number
        else:
            return "The issue number must be positive"
            
    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")
        
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

