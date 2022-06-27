from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date

from app.sql_db import Base


class Book(Base):
  __tablename__ = "books"

  bookID = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  average_rating = Column(Float)
  isbn = Column(String)
  isbn13 = Column(String)
  language_code = Column(Integer, ForeignKey("language_codes.languageCodeID"))
  num_pages = Column(Integer)
  ratings_count = Column(Integer)
  publication_date = Column(Date)
  fk_publisher = Column(Integer, ForeignKey("publishers.publisherID"))
