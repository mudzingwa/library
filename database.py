import sqlite3
from contextlib import closing

from objects import Book
from objects import Publisher

conn = sqlite3.connect('books.db')
conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()
        
#c = conn.cursor()


def add_book(book):
    sql = '''INSERT INTO Book (publisher_id, book_name, year, price) VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (book.publisher_id, book.book_name, book.year, book.price))
        conn.commit()




def update_price(book):
    fetch = '''SELECT * FROM Book WHERE book_name=?'''
    with closing(conn.cursor()) as c:
        c.execute(fetch, (book.book_name,))
        books = c.fetchall()

    for book_data in books:
        book_id = book_data[0]
        sql = '''UPDATE Book SET price=? WHERE book_id=?'''
        with closing(conn.cursor()) as c:
            c.execute(sql, (book.price, book_id))
            conn.commit()




            
def delete_book(book):
    sql = '''DELETE FROM Book WHERE book_id=?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (book.id,))
        conn.commit()


