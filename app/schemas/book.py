from pydantic import BaseModel


class BookBase(BaseModel):
  pass


class BookCreate(BookBase):
  pass


class Book(BookBase):
  pass

  class Config:
    orm_mode = True