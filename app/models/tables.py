from sqlalchemy import Column, ForeignKey, Integer, Table

books_authors_table = Table(
  "books_authors", 
  Column('id', Integer, primary_key=True),
  Column('bookID', Integer, ForeignKey('books.bookID')),
  Column('authorID', Integer, ForeignKey('authors.authorID'))
)