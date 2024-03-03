#Importing types for database
from typing import List
# SQL alchemy imports
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# flask login imports
from flask_login import UserMixin

# initializing Sql database
class Base(DeclarativeBase):
    pass

# Create a link
db = SQLAlchemy(model_class=Base)

class User(db.Model, UserMixin):
    __tablename__ = "user_table"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    children: Mapped[List["Child"]] = relationship()

    def get_id(self):
        return (self.user_id)

class Content(db.Model):
    __tablename__ = "content_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    Content: Mapped[str]
    children: Mapped[List["Child"]] = relationship()

class Child(db.Model):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.user_id"))
    Content_one: Mapped[int] = mapped_column(ForeignKey("content_table.id"))
    Content_two: Mapped[int]
    Content_three: Mapped[int]
