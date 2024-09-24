from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Text, UUID, UniqueConstraint, Uuid, text
from sqlalchemy.orm.base import Mapped
from sqlmodel import Field, Relationship, SQLModel

class Customers(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('customerid', name='customers_pkey'),
        UniqueConstraint('email', name='customers_email_key')
    )

    customerid: UUID = Field(sa_column=mapped_column('customerid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=mapped_column('name', String(255), nullable=False))
    email: Optional[str] = Field(default=None, sa_column=mapped_column('email', String(255)))
    phonenumber: Optional[str] = Field(default=None, sa_column=mapped_column('phonenumber', String(20)))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', Text))
    paidinadvance: Optional[Decimal] = Field(default=None, sa_column=mapped_column('paidinadvance', Numeric(10, 2), server_default=text('0')))
    balance: Optional[Decimal] = Field(default=None, sa_column=mapped_column('balance', Numeric(10, 2), server_default=text('0')))
    paid: Optional[Decimal] = Field(default=None, sa_column=mapped_column('paid', Numeric(10, 2), server_default=text('0')))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    payments: List['Payments'] = Relationship(back_populates='customers')
    projects: List['Projects'] = Relationship(back_populates='customers')


class Roles(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('roleid', name='roles_pkey'),
        UniqueConstraint('name', name='roles_name_key')
    )

    roleid: UUID = Field(sa_column=mapped_column('roleid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=mapped_column('name', String(255), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    users: List['Users'] = Relationship(back_populates='roles')


class Teams(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('teamid', name='teams_pkey'),
    )

    teamid: UUID = Field(sa_column=mapped_column('teamid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=mapped_column('name', String(255), nullable=False))
    specialization: Optional[str] = Field(default=None, sa_column=mapped_column('specialization', String(255)))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    projectteams: List['Projectteams'] = Relationship(back_populates='teams')


class Vendors(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('vendorid', name='vendors_pkey'),
    )

    vendorid: UUID = Field(sa_column=mapped_column('vendorid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=mapped_column('name', String(255), nullable=False))
    contactemail: Optional[str] = Field(default=None, sa_column=mapped_column('contactemail', String(255)))
    contactphone: Optional[str] = Field(default=None, sa_column=mapped_column('contactphone', String(20)))
    address: Optional[str] = Field(default=None, sa_column=mapped_column('address', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    materials: List['Materials'] = Relationship(back_populates='vendors')
    vendorpayments: List['Vendorpayments'] = Relationship(back_populates='vendors')


class Materials(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['vendorid'], ['vendors.vendorid'], name='materials_vendorid_fkey'),
        PrimaryKeyConstraint('materialid', name='materials_pkey')
    )

    materialid: UUID = Field(sa_column=mapped_column('materialid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=mapped_column('name', String(255), nullable=False))
    vendorid: Optional[UUID] = Field(default=None, sa_column=mapped_column('vendorid', Uuid))
    unitprice: Optional[Decimal] = Field(default=None, sa_column=mapped_column('unitprice', Numeric(10, 2)))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    vendors: Optional['Vendors'] = Relationship(back_populates='materials')


class Payments(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['customers.customerid'], name='payments_customerid_fkey'),
        PrimaryKeyConstraint('paymentid', name='payments_pkey')
    )

    paymentid: UUID = Field(sa_column=mapped_column('paymentid', Uuid, server_default=text('uuid_generate_v4()')))
    amount: Decimal = Field(sa_column=mapped_column('amount', Numeric(10, 2), nullable=False))
    paymentdate: date = Field(sa_column=mapped_column('paymentdate', Date, nullable=False))
    customerid: Optional[UUID] = Field(default=None, sa_column=mapped_column('customerid', Uuid))
    paymentmethod: Optional[str] = Field(default=None, sa_column=mapped_column('paymentmethod', String(255)))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    customers: Optional['Customers'] = Relationship(back_populates='payments')


class Projects(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['customers.customerid'], name='projects_customerid_fkey'),
        PrimaryKeyConstraint('projectid', name='projects_pkey')
    )

    projectid: UUID = Field(sa_column=mapped_column('projectid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=mapped_column('name', String(255), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    customerid: Optional[UUID] = Field(default=None, sa_column=mapped_column('customerid', Uuid))
    sitelocation: Optional[str] = Field(default=None, sa_column=mapped_column('sitelocation', Text))
    budget: Optional[Decimal] = Field(default=None, sa_column=mapped_column('budget', Numeric(15, 2)))
    startdate: Optional[date] = Field(default=None, sa_column=mapped_column('startdate', Date))
    enddate: Optional[date] = Field(default=None, sa_column=mapped_column('enddate', Date))
    progress: Optional[str] = Field(default=None, sa_column=mapped_column('progress', String(255)))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

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

    userid: UUID = Field(sa_column=mapped_column('userid', Uuid, server_default=text('uuid_generate_v4()')))
    firstname: str = Field(sa_column=mapped_column('firstname', String(255), nullable=False))
    lastname: str = Field(sa_column=mapped_column('lastname', String(255), nullable=False))
    email: str = Field(sa_column=mapped_column('email', String(255), nullable=False))
    password: str = Field(sa_column=mapped_column('password', String(255), nullable=False))
    roleid: Optional[UUID] = Field(default=None, sa_column=mapped_column('roleid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    roles: Optional['Roles'] = Relationship(back_populates='users')
    employees: List['Employees'] = Relationship(back_populates='users')


class Employees(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['userid'], ['users.userid'], name='employees_userid_fkey'),
        PrimaryKeyConstraint('employeeid', name='employees_pkey'),
        UniqueConstraint('email', name='employees_email_key')
    )

    employeeid: UUID = Field(sa_column=mapped_column('employeeid', Uuid, server_default=text('uuid_generate_v4()')))
    firstname: str = Field(sa_column=mapped_column('firstname', String(255), nullable=False))
    lastname: str = Field(sa_column=mapped_column('lastname', String(255), nullable=False))
    email: Optional[str] = Field(default=None, sa_column=mapped_column('email', String(255)))
    phonenumber: Optional[str] = Field(default=None, sa_column=mapped_column('phonenumber', String(20)))
    position: Optional[str] = Field(default=None, sa_column=mapped_column('position', String(255)))
    salary: Optional[Decimal] = Field(default=None, sa_column=mapped_column('salary', Numeric(10, 2)))
    advancegetamount: Optional[Decimal] = Field(default=None, sa_column=mapped_column('advancegetamount', Numeric(10, 2), server_default=text('0')))
    userid: Optional[UUID] = Field(default=None, sa_column=mapped_column('userid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    users: Optional['Users'] = Relationship(back_populates='employees')
    empworklog: List['Empworklog'] = Relationship(back_populates='employees')


class Plans(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='plans_projectid_fkey'),
        PrimaryKeyConstraint('planid', name='plans_pkey')
    )

    planid: UUID = Field(sa_column=mapped_column('planid', Uuid, server_default=text('uuid_generate_v4()')))
    name: str = Field(sa_column=mapped_column('name', String(255), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=mapped_column('description', Text))
    projectid: Optional[UUID] = Field(default=None, sa_column=mapped_column('projectid', Uuid))
    blueprint: Optional[str] = Field(default=None, sa_column=mapped_column('blueprint', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='plans')


class Projectpayments(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='projectpayments_projectid_fkey'),
        PrimaryKeyConstraint('projectpaymentid', name='projectpayments_pkey')
    )

    projectpaymentid: UUID = Field(sa_column=mapped_column('projectpaymentid', Uuid, server_default=text('uuid_generate_v4()')))
    amount: Decimal = Field(sa_column=mapped_column('amount', Numeric(10, 2), nullable=False))
    paymentdate: date = Field(sa_column=mapped_column('paymentdate', Date, nullable=False))
    projectid: Optional[UUID] = Field(default=None, sa_column=mapped_column('projectid', Uuid))
    paymentmethod: Optional[str] = Field(default=None, sa_column=mapped_column('paymentmethod', String(255)))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='projectpayments')


class Projectstatus(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='projectstatus_projectid_fkey'),
        PrimaryKeyConstraint('projectstatusid', name='projectstatus_pkey')
    )

    projectstatusid: UUID = Field(sa_column=mapped_column('projectstatusid', Uuid, server_default=text('uuid_generate_v4()')))
    status: str = Field(sa_column=mapped_column('status', String(255), nullable=False))
    projectid: Optional[UUID] = Field(default=None, sa_column=mapped_column('projectid', Uuid))
    comments: Optional[str] = Field(default=None, sa_column=mapped_column('comments', Text))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='projectstatus')


class Projectteams(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='projectteams_projectid_fkey'),
        ForeignKeyConstraint(['teamid'], ['teams.teamid'], name='projectteams_teamid_fkey'),
        PrimaryKeyConstraint('projectid', 'teamid', name='projectteams_pkey')
    )

    projectid: UUID = Field(sa_column=mapped_column('projectid', Uuid, nullable=False))
    teamid: UUID = Field(sa_column=mapped_column('teamid', Uuid, nullable=False))
    assigneddate: Optional[date] = Field(default=None, sa_column=mapped_column('assigneddate', Date))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='projectteams')
    teams: Optional['Teams'] = Relationship(back_populates='projectteams')


class Vendorpayments(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='vendorpayments_projectid_fkey'),
        ForeignKeyConstraint(['vendorid'], ['vendors.vendorid'], name='vendorpayments_vendorid_fkey'),
        PrimaryKeyConstraint('vendorpaymentid', name='vendorpayments_pkey')
    )

    vendorpaymentid: UUID = Field(sa_column=mapped_column('vendorpaymentid', Uuid, server_default=text('uuid_generate_v4()')))
    amount: Decimal = Field(sa_column=mapped_column('amount', Numeric(10, 2), nullable=False))
    paymentdate: date = Field(sa_column=mapped_column('paymentdate', Date, nullable=False))
    vendorid: Optional[UUID] = Field(default=None, sa_column=mapped_column('vendorid', Uuid))
    projectid: Optional[UUID] = Field(default=None, sa_column=mapped_column('projectid', Uuid))
    paymentmethod: Optional[str] = Field(default=None, sa_column=mapped_column('paymentmethod', String(255)))
    status: Optional[str] = Field(default=None, sa_column=mapped_column('status', String(255), server_default=text("'Pending'::character varying")))
    paidinadvance: Optional[Decimal] = Field(default=None, sa_column=mapped_column('paidinadvance', Numeric(10, 2), server_default=text('0')))
    balance: Optional[Decimal] = Field(default=None, sa_column=mapped_column('balance', Numeric(10, 2), server_default=text('0')))
    paid: Optional[Decimal] = Field(default=None, sa_column=mapped_column('paid', Numeric(10, 2), server_default=text('0')))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    projects: Optional['Projects'] = Relationship(back_populates='vendorpayments')
    vendors: Optional['Vendors'] = Relationship(back_populates='vendorpayments')


class Empworklog(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['employeeid'], ['employees.employeeid'], name='empworklog_employeeid_fkey'),
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='empworklog_projectid_fkey'),
        PrimaryKeyConstraint('worklogid', name='empworklog_pkey')
    )

    worklogid: UUID = Field(sa_column=mapped_column('worklogid', Uuid, server_default=text('uuid_generate_v4()')))
    workhours: int = Field(sa_column=mapped_column('workhours', Integer, nullable=False))
    workdate: date = Field(sa_column=mapped_column('workdate', Date, nullable=False))
    employeeid: Optional[UUID] = Field(default=None, sa_column=mapped_column('employeeid', Uuid))
    projectid: Optional[UUID] = Field(default=None, sa_column=mapped_column('projectid', Uuid))
    taskdescription: Optional[str] = Field(default=None, sa_column=mapped_column('taskdescription', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[UUID] = Field(default=None, sa_column=mapped_column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=mapped_column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    updatedby: Optional[UUID] = Field(default=None, sa_column=mapped_column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=mapped_column('isactive', Boolean, server_default=text('true')))

    employees: Optional['Employees'] = Relationship(back_populates='empworklog')
    projects: Optional['Projects'] = Relationship(back_populates='empworklog')
