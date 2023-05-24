import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

'''
import sqlite3
from database import add_book
from database import update_price
from database import delete_book
from database import list_books
'''

import database
from objects import Book

def display_menu():
    print("COMMAND MENU")
    print("list  - List the books in the database")
    print("add  - Add a book to the database")
    print("update - Update price of a book using book name")
    print("del  - Delete a book using Book ID")
    print("end  - Exit the application")
    print()
    print("Enter a command:")

    
def add():
    
    root = tk.Tk()
    root.title("Add Book UI")
    root.geometry("900x600")

    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.pack(fill=tk.BOTH, expand=True)

    def add_books():
        publisher_id = publisherEntry.get()
        book_name = bookNameEntry.get()
        year = yearEntry.get()
        price = priceEntry.get()

        book = Book(publisher_id=publisher_id, book_name=book_name, year=year, price=price)
        database.add_book(book)
        commentLabel.config(text="Record successfully added!!")
        

        
    def clear():
        publisherEntry.delete(0, END)
        bookNameEntry.delete(0, END)
        yearEntry.delete(0, END)
        priceEntry.delete(0, END)
        commentLabel.config(text=" ")

    def exitWindow():
        main()
        root.destroy()
        

    publisherLabel = ttk.Label(frame, text="Publisher ID: ")
    bookNameLabel = ttk.Label(frame, text="Book Name: ")
    yearLabel = ttk.Label(frame, text="Year: ")
    priceLabel = ttk.Label(frame, text="Price: ")

    publisherLabel.grid(row=0, column=0, sticky=W, pady=2)
    bookNameLabel.grid(row=1, column=0, sticky=W, pady=2)
    yearLabel.grid(row=2, column=0, sticky=W, pady=2)
    priceLabel.grid(row=3, column=0, sticky=W, pady=2)

    publisherText = tk.StringVar()
    publisherEntry = ttk.Entry(frame, width=25, textvariable=publisherText)

    bookNameText = tk.StringVar()
    bookNameEntry = ttk.Entry(frame, width=25, textvariable=bookNameText)

    yearText = tk.StringVar()
    yearEntry = ttk.Entry(frame, width=25, textvariable=yearText)

    priceText = tk.StringVar()
    priceEntry = ttk.Entry(frame, width=25, textvariable=priceText)

    publisherEntry.grid(row=0, column=1, pady=2)
    bookNameEntry.grid(row=1, column=1, pady=2)
    yearEntry.grid(row=2, column=1, pady=2)
    priceEntry.grid(row=3, column=1, pady=2)

    addButton = ttk.Button(frame, text="ADD", command=add_books)
    clearButton = ttk.Button(frame, text="CLEAR", command = clear)
    exitButton = ttk.Button(frame, text="EXIT", command=exitWindow)

    addButton.grid(row=4, column=0, sticky=W, pady=2)
    clearButton.grid(row=4, column=1, sticky=W, pady=2)
    exitButton.grid(row=8, column=4, sticky=W, pady=2)

    commentLabel=ttk.Label(frame, text="Record successfully added!!")
    commentLabel.grid(row=6, column=0, sticky=W, pady=2)
    commentLabel.config(text=" ")

    root.mainloop()


def update():
    root = tk.Tk()
    root.title("Update Price UI")
    root.geometry("900x600")

    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.pack(fill=tk.BOTH, expand=True)

    def updateprice():
        book_name = bookNameEntry.get()
        new_price = priceEntry.get()
        book = Book(book_name=book_name, price=new_price)
        database.update_price(book)
        commentLabel.config(text="Price successfully updated!")


    def clear():
        bookNameEntry.delete(0, END)
        priceEntry.delete(0, END)
        commentLabel.config(text=" ")

    def exitWindow():
        main()
        root.destroy()
        



    bookNameLabel = ttk.Label(frame, text="Book Name: ")
    priceLabel = ttk.Label(frame, text="Price: ")

    bookNameLabel.grid(row=0, column=0, sticky=W, pady=2)
    priceLabel.grid(row=1, column=0, sticky=W, pady=2)

    bookNameText = tk.StringVar()
    bookNameEntry = ttk.Entry(frame, width=25, textvariable=bookNameText)

    priceText = tk.StringVar()
    priceEntry = ttk.Entry(frame, width=25, textvariable=priceText)

    bookNameEntry.grid(row=0, column=1, pady=2)
    priceEntry.grid(row=1, column=1, pady=2)

    updateButton = ttk.Button(frame, text="UPDATE", command=updateprice)
    clearButton = ttk.Button(frame, text="CLEAR", command=clear)
    exitButton = ttk.Button(frame, text="EXIT", command=exitWindow)

    updateButton.grid(row=2, column=0, sticky=W, pady=2)
    clearButton.grid(row=2, column=1, sticky=W, pady=2)
    exitButton.grid(row=8, column=4, sticky=W, pady=2)

    commentLabel=ttk.Label(frame, text="Record successfully added!!")
    commentLabel.grid(row=6, column=0, sticky=W, pady=2)
    commentLabel.config(text=" ")

    root.mainloop()

def delete():
    root = tk.Tk()
    root.title("Delete Book UI")
    root.geometry("900x600")

    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.pack(fill=tk.BOTH, expand=True)

    def deletebook():
        book_id = bookIDEntry.get()
        book = Book(id=book_id)
        database.delete_book(book)
        commentLabel.config(text="Book Successfully Deleted!")

       

    def clear():
        bookIDEntry.delete(0, END)
        commentLabel.config(text=" ")

    def exitWindow():
        main()
        root.destroy()
        

        
    bookIDLabel = ttk.Label(frame, text="Book ID: ")
    bookIDLabel.grid(row=0, column=0, sticky=W, pady=2)

    bookIDText = tk.StringVar()
    bookIDEntry = ttk.Entry(frame, width=25, textvariable=bookIDText)

    bookIDEntry.grid(row=0, column=1, pady=2)

    deleteButton = ttk.Button(frame, text="DELETE", command=deletebook)
    clearButton = ttk.Button(frame, text="CLEAR", command=clear)
    exitButton = ttk.Button(frame, text="EXIT", command=exitWindow)

    deleteButton.grid(row=1, column=0, sticky=W, pady=2)
    clearButton.grid(row=1, column=1, sticky=W, pady=2)
    exitButton.grid(row=8, column=4, sticky=W, pady=2)

    commentLabel=ttk.Label(frame, text="Record successfully added!!")
    commentLabel.grid(row=6, column=0, sticky=W, pady=2)
    commentLabel.config(text=" ")

    root.mainloop()


#add()
#update()
#delete()

def main():
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "list":
            list_books()
        elif command == "add":
            add()
        elif command == "update":
            update()
        elif command == "del":
            delete()
        elif command == "end":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    print("Bye!")

if __name__ == "__main__":
    main()

