from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.sql_db import Base


class Publisher(Base):
  __tablename__ = "publishers"

  publisherID = Column(Integer, primary_key=True, index=True)
  name = Column(String)
