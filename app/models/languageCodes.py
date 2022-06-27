from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.sql_db import Base


class LanguageCode(Base):
  __tablename__ = "language_codes"

  languageCodeID = Column(Integer, primary_key=True, index=True)
  code = Column(String)
