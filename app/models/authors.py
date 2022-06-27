from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.sql_db import Base


class Author(Base):
  __tablename__ = "authors"

  authorID = Column(Integer, primary_key=True, index=True)
  name = Column(String)
