from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Foreignkeyconstraint, Index, String
from sqlalchemy.orm.base import Mapped
from sqlmodel import Field, Relationship, SQLModel 


metadata = SQLModel.metadata