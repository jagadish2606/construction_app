from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional
import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Text, UUID, UniqueConstraint, Uuid, column, text
from sqlalchemy.orm.base import Mapped
from sqlmodel import Field, Relationship, SQLModel

class Customers(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('customerid', name='customers_pkey'),
        UniqueConstraint('email', name='customers_email_key')
    )

    customerid: uuid.UUID = Field(sa_column=Column(Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=Column('name', String(255), nullable=False))
    email: Optional[str] = Field(default=None, sa_column=Column('email', String(255)))
    phonenumber: Optional[str] = Field(default=None, sa_column=Column('phonenumber', String(20)))
    address: Optional[str] = Field(default=None, sa_column=Column('address', Text))
    paidinadvance: Optional[Decimal] = Field(default=None, sa_column=Column('paidinadvance', Numeric(10, 2), server_default=text('0')))
    balance: Optional[Decimal] = Field(default=None, sa_column=Column('balance', Numeric(10, 2), server_default=text('0')))
    paid: Optional[Decimal] = Field(default=None, sa_column=Column('paid', Numeric(10, 2), server_default=text('0')))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    payments: List['Payments'] = Relationship(back_populates='customers')
    projects: List['Projects'] = Relationship(back_populates='customers')

    class Config:
        arbitrary_types_allowed = True  # Allow arbitrary types


class Roles(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('roleid', name='roles_pkey'),
        UniqueConstraint('name', name='roles_name_key')
    )

    roleid: uuid.UUID = Field(sa_column=Column('roleid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=Column('name', String(255), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    users: List['Users'] = Relationship(back_populates='roles')


class Teams(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('teamid', name='teams_pkey'),
    )

    teamid: uuid.UUID = Field(sa_column=Column('teamid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=Column('name', String(255), nullable=False))
    specialization: Optional[str] = Field(default=None, sa_column=Column('specialization', String(255)))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    projectteams: List['Projectteams'] = Relationship(back_populates='teams')


class Vendors(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('vendorid', name='vendors_pkey'),
    )

    vendorid: uuid.UUID = Field(sa_column=Column('vendorid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=Column('name', String(255), nullable=False))
    contactemail: Optional[str] = Field(default=None, sa_column=Column('contactemail', String(255)))
    contactphone: Optional[str] = Field(default=None, sa_column=Column('contactphone', String(20)))
    address: Optional[str] = Field(default=None, sa_column=Column('address', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    materials: List['Materials'] = Relationship(back_populates='vendors')
    vendorpayments: List['Vendorpayments'] = Relationship(back_populates='vendors')


class Materials(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['vendorid'], ['vendors.vendorid'], name='materials_vendorid_fkey'),
        PrimaryKeyConstraint('materialid', name='materials_pkey')
    )

    materialid: uuid.UUID = Field(sa_column=Column('materialid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=Column('name', String(255), nullable=False))
    vendorid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('vendorid', Uuid))
    unitprice: Optional[Decimal] = Field(default=None, sa_column=Column('unitprice', Numeric(10, 2)))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    vendors: Optional['Vendors'] = Relationship(back_populates='materials')


class Payments(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['customers.customerid'], name='payments_customerid_fkey'),
        PrimaryKeyConstraint('paymentid', name='payments_pkey')
    )

    paymentid: uuid.UUID = Field(sa_column=Column('paymentid', Uuid, server_default=text('uuid_generate_v4()')))
    amount: Decimal = Field(sa_column=Column('amount', Numeric(10, 2), nullable=False))
    paymentdate: date = Field(sa_column=Column('paymentdate', Date, nullable=False))
    customerid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('customerid', Uuid))
    paymentmethod: Optional[str] = Field(default=None, sa_column=Column('paymentmethod', String(255)))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    customers: Optional['Customers'] = Relationship(back_populates='payments')


class Projects(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['customers.customerid'], name='projects_customerid_fkey'),
        PrimaryKeyConstraint('projectid', name='projects_pkey')
    )

    projectid: uuid.UUID = Field(sa_column=Column('projectid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=Column('name', String(255), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
    customerid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('customerid', Uuid))
    sitelocation: Optional[str] = Field(default=None, sa_column=Column('sitelocation', Text))
    budget: Optional[Decimal] = Field(default=None, sa_column=Column('budget', Numeric(15, 2)))
    startdate: Optional[date] = Field(default=None, sa_column=Column('startdate', Date))
    enddate: Optional[date] = Field(default=None, sa_column=Column('enddate', Date))
    progress: Optional[str] = Field(default=None, sa_column=Column('progress', String(255)))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    customers: Optional['Customers'] = Relationship(back_populates='projects')
    plans: List['Plans'] = Relationship(back_populates='projects')
    projectpayments: List['Projectpayments'] = Relationship(back_populates='projects')
    projectstatus: List['Projectstatus'] = Relationship(back_populates='projects')
    projectteams: List['Projectteams'] = Relationship(back_populates='projects')
    vendorpayments: List['Vendorpayments'] = Relationship(back_populates='projects')
    empworklog: List['Empworklog'] = Relationship(back_populates='projects')


class Users(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['roleid'], ['roles.roleid'], name='users_roleid_fkey'),
        PrimaryKeyConstraint('userid', name='users_pkey'),
        UniqueConstraint('email', name='users_email_key')
    )

    userid: uuid.UUID = Field(sa_column=Column('userid', Uuid, server_default=text('uuid_generate_v4()')))
    firstname: str = Field(sa_column=Column('firstname', String(255), nullable=False))
    lastname: str = Field(sa_column=Column('lastname', String(255), nullable=False))
    email: str = Field(sa_column=Column('email', String(255), nullable=False))
    password: str = Field(sa_column=Column('password', String(255), nullable=False))
    roleid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('roleid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    roles: Optional['Roles'] = Relationship(back_populates='users')
    employees: List['Employees'] = Relationship(back_populates='users')


class Employees(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['userid'], ['users.userid'], name='employees_userid_fkey'),
        PrimaryKeyConstraint('employeeid', name='employees_pkey'),
        UniqueConstraint('email', name='employees_email_key')
    )

    employeeid: uuid.UUID = Field(sa_column=Column('employeeid', Uuid, server_default=text('uuid_generate_v4()')))
    firstname: str = Field(sa_column=Column('firstname', String(255), nullable=False))
    lastname: str = Field(sa_column=Column('lastname', String(255), nullable=False))
    email: Optional[str] = Field(default=None, sa_column=Column('email', String(255)))
    phonenumber: Optional[str] = Field(default=None, sa_column=Column('phonenumber', String(20)))
    position: Optional[str] = Field(default=None, sa_column=Column('position', String(255)))
    salary: Optional[Decimal] = Field(default=None, sa_column=Column('salary', Numeric(10, 2)))
    advancegetamount: Optional[Decimal] = Field(default=None, sa_column=Column('advancegetamount', Numeric(10, 2), server_default=text('0')))
    userid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('userid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    users: Optional['Users'] = Relationship(back_populates='employees')
    empworklog: List['Empworklog'] = Relationship(back_populates='employees')


class Plans(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='plans_projectid_fkey'),
        PrimaryKeyConstraint('planid', name='plans_pkey')
    )

    planid: uuid.UUID = Field(sa_column=Column('planid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=Column('name', String(255), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
    projectid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
    blueprint: Optional[str] = Field(default=None, sa_column=Column('blueprint', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='plans')


class Projectpayments(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='projectpayments_projectid_fkey'),
        PrimaryKeyConstraint('projectpaymentid', name='projectpayments_pkey')
    )

    projectpaymentid: uuid.UUID = Field(sa_column=Column('projectpaymentid', Uuid, server_default=text('uuid_generate_v4()')))
    amount: Decimal = Field(sa_column=Column('amount', Numeric(10, 2), nullable=False))
    paymentdate: date = Field(sa_column=Column('paymentdate', Date, nullable=False))
    projectid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
    paymentmethod: Optional[str] = Field(default=None, sa_column=Column('paymentmethod', String(255)))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='projectpayments')


class Projectstatus(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='projectstatus_projectid_fkey'),
        PrimaryKeyConstraint('projectstatusid', name='projectstatus_pkey')
    )

    projectstatusid: uuid.UUID = Field(sa_column=Column('projectstatusid', Uuid, server_default=text('uuid_generate_v4()')))
    status: str = Field(sa_column=Column('status', String(255), nullable=False))
    projectid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
    comments: Optional[str] = Field(default=None, sa_column=Column('comments', Text))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='projectstatus')


class Projectteams(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='projectteams_projectid_fkey'),
        ForeignKeyConstraint(['teamid'], ['teams.teamid'], name='projectteams_teamid_fkey'),
        PrimaryKeyConstraint('projectid', 'teamid', name='projectteams_pkey')
    )

    projectid: uuid.UUID = Field(sa_column=Column('projectid', Uuid, nullable=False))
    teamid: uuid.UUID = Field(sa_column=Column('teamid', Uuid, nullable=False))
    assigneddate: Optional[date] = Field(default=None, sa_column=Column('assigneddate', Date))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='projectteams')
    teams: Optional['Teams'] = Relationship(back_populates='projectteams')


class Vendorpayments(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='vendorpayments_projectid_fkey'),
        ForeignKeyConstraint(['vendorid'], ['vendors.vendorid'], name='vendorpayments_vendorid_fkey'),
        PrimaryKeyConstraint('vendorpaymentid', name='vendorpayments_pkey')
    )

    vendorpaymentid: uuid.UUID = Field(sa_column=Column('vendorpaymentid', Uuid, server_default=text('uuid_generate_v4()')))
    amount: Decimal = Field(sa_column=Column('amount', Numeric(10, 2), nullable=False))
    paymentdate: date = Field(sa_column=Column('paymentdate', Date, nullable=False))
    vendorid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('vendorid', Uuid))
    projectid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
    paymentmethod: Optional[str] = Field(default=None, sa_column=Column('paymentmethod', String(255)))
    status: Optional[str] = Field(default=None, sa_column=Column('status', String(255), server_default=text("'Pending'::character varying")))
    paidinadvance: Optional[Decimal] = Field(default=None, sa_column=Column('paidinadvance', Numeric(10, 2), server_default=text('0')))
    balance: Optional[Decimal] = Field(default=None, sa_column=Column('balance', Numeric(10, 2), server_default=text('0')))
    paid: Optional[Decimal] = Field(default=None, sa_column=Column('paid', Numeric(10, 2), server_default=text('0')))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='vendorpayments')
    vendors: Optional['Vendors'] = Relationship(back_populates='vendorpayments')


class Empworklog(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['employeeid'], ['employees.employeeid'], name='empworklog_employeeid_fkey'),
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='empworklog_projectid_fkey'),
        PrimaryKeyConstraint('worklogid', name='empworklog_pkey')
    )

    worklogid: uuid.UUID = Field(sa_column=Column('worklogid', Uuid, server_default=text('uuid_generate_v4()')))
    workhours: int = Field(sa_column=Column('workhours', Integer, nullable=False))
    workdate: date = Field(sa_column=Column('workdate', Date, nullable=False))
    employeeid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('employeeid', Uuid))
    projectid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
    taskdescription: Optional[str] = Field(default=None, sa_column=Column('taskdescription', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    employees: Optional['Employees'] = Relationship(back_populates='empworklog')
    projects: Optional['Projects'] = Relationship(back_populates='empworklog')
