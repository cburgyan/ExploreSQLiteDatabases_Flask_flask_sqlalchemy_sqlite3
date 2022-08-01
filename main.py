import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session


# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()

# cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)')
# cursor.execute('INSERT INTO books VALUES(1, "Harry Potter", "J.K. Rowling", "9.3")')
# db.commit()

# Create Flask Object
app = Flask(__name__)

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db2 = SQLAlchemy(app)


# Define Table/Record
class Book(db2.Model):
    id = db2.Column(db2.Integer, primary_key=True)
    title = db2.Column(db2.String(250), unique=True, nullable=False)
    author = db2.Column(db2.String(250), nullable=False)
    rating = db2.Column(db2.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# Create Table
# db2.create_all()


# Create Record in Table
# new_book = Book(id=1, title='Harry Potter', author='J.K. Rowling', rating=9.3)
# db2.session.add(new_book)
# db2.session.commit()


# Create 2nd Record
# new_book2 = Book(id=2, title='Harry Potter and the Chamber of Secrets', author='J.K. Rowling', rating=9.1)
# db2.session.add(new_book2)
# db2.session.commit()

# Read All Records
all_books = Book.query.all()
print(all_books)

# Read a Particular Record By Query
book = Book.query.filter_by(title="Harry Potter and the Sorceror's Stone").first()
print(type(book))
print(book)

# Update A Particular Record By Query
# book_to_update = Book.query.filter_by(title='Harry Potter').first()
# book_to_update.title = "Harry Potter and the Sorceror's Stone"
# db2.session.commit()


# Update a Particular Record By Primary Key
# book_id = 1
# book_to_update = Book.query.filter_by(id=book_id).first()
# book_to_update.rating = 9.4
# db2.session.commit()

# Delete Record
# new_book3 = Book(id=3, title='Harry Potter and the Magical Umbrella', author='J.K. Rowling', rating=8.9)
# db2.session.add(new_book3)
# db2.session.commit()
# book_to_delete = Book.query.filter_by(title='Harry Potter and the Magical Umbrella').first()
# print(book_to_delete)
# db2.session.delete(book_to_delete)
# db2.session.commit()
