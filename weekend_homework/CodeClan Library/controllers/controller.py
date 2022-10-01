
from crypt import methods
from turtle import st
from flask import render_template, request, redirect
from app import app
from models.book_list import *
import datetime

#when browser hit route trigger func(bundle)
#default method - GET
@app.route("/books")
def books():
    #give to render object template,also reference to our list and variable
    return render_template("index.html",book_list=book_list, title="CodeClan Library")

@app.route("/books/<index>")
def book_by_id(index):
    #everithing from ouside comming as string! (<index>)
    choosen_book = find_book_by_index(index)
    return render_template("choosen_book.html", book = choosen_book, index=index)

@app.route("/books/<index>", methods=["POST"])
def put_to_book(index):
         book = find_book_by_index(index)
         book.checked_out = True if "checked_out" in request.form else False

         return redirect("/books")

        


@app.route("/books", methods=["POST"])
def add_book():
    #create new book obj, invoke func for add him into the list
    #get arguments and give it constructor - use request.form[]
    #key-value pair (<input name="blq blq">) pass name like key into request.form to get his value comming from ouside world
    
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    #get true if is checked
    checked_out = True if "checked_out" in request.form else False
    #deal with date
    return_by_date = request.form["return_by_date"]
    split_date = return_by_date.split("/")
    return_by_date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    #naming atr - order doesn't maters
    new_book = Book(title=title, author=author, genre=genre, checked_out=checked_out, return_by_date=return_by_date)
    add_book_to_list(new_book)
    return redirect("/books")

@app.route("/books/delete/<title>",methods=["POST"])
def delete_book_by_title(title):
    #invoke del funk with given title from outside world
    del_book_by_title(title)
    return redirect("/books")
