from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Text, UUID, UniqueConstraint, Uuid, text
from sqlalchemy.orm.base import Mapped
from sqlmodel import Field, Relationship, SQLModel

class Customer(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('customerid', name='customer_pkey'),
    )

    customerid: UUID = Field(sa_column=mapped_column('customerid', Uuid, server_default=text('gen_random_uuid()')))
    name: str = Field(sa_column=mapped_column('name', String(100), nullable=False))
    email: Optional[str] = Field(default=None, sa_column=mapped_column('email', String(100)))
    phone: Optional[str] = Field(default=None, sa_column=mapped_column('phone', String(15)))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))

    projects: List['Projects'] = Relationship(back_populates='customer')
    payments: List['Payments'] = Relationship(back_populates='customer')


class Employee(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['roleid'], ['role.roleid'], name='employee_roleid_fkey'),
        ForeignKeyConstraint(['teamid'], ['team.teamid'], name='employee_teamid_fkey'),
        ForeignKeyConstraint(['userid'], ['users.userid'], name='employee_userid_fkey'),
        PrimaryKeyConstraint('employeeid', name='employee_pkey')
    )

    employeeid: UUID = Field(sa_column=mapped_column('employeeid', Uuid, server_default=text('gen_random_uuid()')))
    fullname: str = Field(sa_column=mapped_column('fullname', String(100), nullable=False))
    userid: Optional[UUID] = Field(default=None, sa_column=mapped_column('userid', Uuid))
    phonenumber: Optional[str] = Field(default=None, sa_column=mapped_column('phonenumber', String(15)))
    email: Optional[str] = Field(default=None, sa_column=mapped_column('email', String(100)))
    teamid: Optional[UUID] = Field(default=None, sa_column=mapped_column('teamid', Uuid))
    roleid: Optional[UUID] = Field(default=None, sa_column=mapped_column('roleid', Uuid))
    joineddate: Optional[date] = Field(default=None, sa_column=mapped_column('joineddate', Date))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    role: Optional['Role'] = Relationship(back_populates='employee')
    team: Optional['Team'] = Relationship(back_populates='employee')
    users: Optional['Users'] = Relationship(back_populates='employee')
    team_: List['Team'] = Relationship(back_populates='employee_')


class Role(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('roleid', name='role_pkey'),
        UniqueConstraint('rolename', name='role_rolename_key')
    )

    roleid: UUID = Field(sa_column=mapped_column('roleid', Uuid, server_default=text('gen_random_uuid()')))
    rolename: str = Field(sa_column=mapped_column('rolename', String(50), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))

    employee: List['Employee'] = Relationship(back_populates='role')
    users: List['Users'] = Relationship(back_populates='role')


class Team(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['leademployeeid'], ['employee.employeeid'], name='fk_team_leademployee'),
        PrimaryKeyConstraint('teamid', name='team_pkey')
    )

    teamid: UUID = Field(sa_column=mapped_column('teamid', Uuid, server_default=text('gen_random_uuid()')))
    teamname: str = Field(sa_column=mapped_column('teamname', String(100), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    leademployeeid: Optional[UUID] = Field(default=None, sa_column=mapped_column('leademployeeid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))

    employee: List['Employee'] = Relationship(back_populates='team')
    employee_: Optional['Employee'] = Relationship(back_populates='team_')
    projects: List['Projects'] = Relationship(back_populates='team')


class Vendor(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('vendorid', name='vendor_pkey'),
    )

    vendorid: UUID = Field(sa_column=mapped_column('vendorid', Uuid, server_default=text('gen_random_uuid()')))
    name: str = Field(sa_column=mapped_column('name', String(100), nullable=False))
    email: Optional[str] = Field(default=None, sa_column=mapped_column('email', String(100)))
    phone: Optional[str] = Field(default=None, sa_column=mapped_column('phone', String(15)))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))

    materials: List['Materials'] = Relationship(back_populates='vendor')
    payments: List['Payments'] = Relationship(back_populates='vendor')


class Projects(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['customer.customerid'], name='projects_customerid_fkey'),
        ForeignKeyConstraint(['teamid'], ['team.teamid'], name='projects_teamid_fkey'),
        PrimaryKeyConstraint('projectid', name='projects_pkey')
    )

    projectid: UUID = Field(sa_column=mapped_column('projectid', Uuid, server_default=text('gen_random_uuid()')))
    name: str = Field(sa_column=mapped_column('name', String(100), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    customerid: Optional[UUID] = Field(default=None, sa_column=mapped_column('customerid', Uuid))
    teamid: Optional[UUID] = Field(default=None, sa_column=mapped_column('teamid', Uuid))
    startdate: Optional[date] = Field(default=None, sa_column=mapped_column('startdate', Date))
    enddate: Optional[date] = Field(default=None, sa_column=mapped_column('enddate', Date))
    status: Optional[str] = Field(default=None, sa_column=mapped_column('status', String(50)))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))

    customer: Optional['Customer'] = Relationship(back_populates='projects')
    team: Optional['Team'] = Relationship(back_populates='projects')
    materials: List['Materials'] = Relationship(back_populates='projects')
    payments: List['Payments'] = Relationship(back_populates='projects')


class Users(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['roleid'], ['role.roleid'], name='users_roleid_fkey'),
        PrimaryKeyConstraint('userid', name='users_pkey'),
        UniqueConstraint('email', name='users_email_key'),
        UniqueConstraint('username', name='users_username_key')
    )

    userid: UUID = Field(sa_column=mapped_column('userid', Uuid, server_default=text('gen_random_uuid()')))
    username: str = Field(sa_column=mapped_column('username', String(50), nullable=False))
    email: str = Field(sa_column=mapped_column('email', String(100), nullable=False))
    password: str = Field(sa_column=mapped_column('password', String(100), nullable=False))
    passwordhash: Optional[str] = Field(default=None, sa_column=mapped_column('passwordhash', Text))
    roleid: Optional[UUID] = Field(default=None, sa_column=mapped_column('roleid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    phonenumber: Optional[str] = Field(default=None, sa_column=mapped_column('phonenumber', String(15)))
    usertype: Optional[str] = Field(default=None, sa_column=mapped_column('usertype', String(50)))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    employee: List['Employee'] = Relationship(back_populates='users')
    role: Optional['Role'] = Relationship(back_populates='users')


class Materials(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='materials_projectid_fkey'),
        ForeignKeyConstraint(['vendorid'], ['vendor.vendorid'], name='materials_vendorid_fkey'),
        PrimaryKeyConstraint('materialid', name='materials_pkey')
    )

    materialid: UUID = Field(sa_column=mapped_column('materialid', Uuid, server_default=text('gen_random_uuid()')))
    name: str = Field(sa_column=mapped_column('name', String(100), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    quantity: Optional[int] = Field(default=None, sa_column=mapped_column('quantity', Integer, server_default=text('0')))
    unitprice: Optional[Decimal] = Field(default=None, sa_column=mapped_column('unitprice', Numeric(10, 2)))
    vendorid: Optional[UUID] = Field(default=None, sa_column=mapped_column('vendorid', Uuid))
    projectid: Optional[UUID] = Field(default=None, sa_column=mapped_column('projectid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))

    projects: Optional['Projects'] = Relationship(back_populates='materials')
    vendor: Optional['Vendor'] = Relationship(back_populates='materials')


class Payments(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['customer.customerid'], name='payments_customerid_fkey'),
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='payments_projectid_fkey'),
        ForeignKeyConstraint(['vendorid'], ['vendor.vendorid'], name='payments_vendorid_fkey'),
        PrimaryKeyConstraint('paymentid', name='payments_pkey')
    )

    paymentid: UUID = Field(sa_column=mapped_column('paymentid', Uuid, server_default=text('gen_random_uuid()')))
    amount: Decimal = Field(sa_column=mapped_column('amount', Numeric(12, 2), nullable=False))
    paymentdate: date = Field(sa_column=mapped_column('paymentdate', Date, nullable=False))
    paymenttype: Optional[str] = Field(default=None, sa_column=mapped_column('paymenttype', String(50)))
    customerid: Optional[UUID] = Field(default=None, sa_column=mapped_column('customerid', Uuid))
    vendorid: Optional[UUID] = Field(default=None, sa_column=mapped_column('vendorid', Uuid))
    projectid: Optional[UUID] = Field(default=None, sa_column=mapped_column('projectid', Uuid))
    remarks: Optional[str] = Field(default=None, sa_column=mapped_column('remarks', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))

    customer: Optional['Customer'] = Relationship(back_populates='payments')
    projects: Optional['Projects'] = Relationship(back_populates='payments')
    vendor: Optional['Vendor'] = Relationship(back_populates='payments')
