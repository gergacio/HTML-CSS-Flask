from models.book import *
import datetime

#create two objects class Book and put them into list   
book_one = Book("How to Think Like a Computer Scientist", "Allen Downey", "sci-fi", False,datetime.date(2022,10,5))
book_two = Book("You don't know JavaScript", "Kyle Simpson", "sci-fi", False, datetime.date(2022,10,6))

book_list = [book_one, book_two]

#methods:
def add_book_to_list(book):
    book_list.append(book)

def del_book_by_title(title):
    for book in book_list:
        if book.title == title:
            book_list.remove(book)

def find_book_by_index(index):
    found_book = book_list[int(index)]
    return found_book







