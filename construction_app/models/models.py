# from datetime import date, datetime
# from decimal import Decimal
# from typing import List, Optional
# import uuid

# from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Text, uuid.UUID, UniqueConstraint, Uuid, column, text
# from sqlalchemy.orm.base import Mapped
# from sqlmodel import Field, Relationship, SQLModel

# class Customers(SQLModel, table=True):
#     __table_args__ = (
#         PrimaryKeyConstraint('customerid', name='customers_pkey'),
#         UniqueConstraint('email', name='customers_email_key')
#     )

#     customerid: uuid.uuid.UUID = Field(sa_column=Column(Uuid, server_default=text('uuid_generate_v4()')))
#     name: str = Field(sa_column=Column('name', String(255), nullable=False))
#     email: Optional[str] = Field(default=None, sa_column=Column('email', String(255)))
#     phonenumber: Optional[str] = Field(default=None, sa_column=Column('phonenumber', String(20)))
#     address: Optional[str] = Field(default=None, sa_column=Column('address', Text))
#     paidinadvance: Optional[Decimal] = Field(default=None, sa_column=Column('paidinadvance', Numeric(10, 2), server_default=text('0')))
#     balance: Optional[Decimal] = Field(default=None, sa_column=Column('balance', Numeric(10, 2), server_default=text('0')))
#     paid: Optional[Decimal] = Field(default=None, sa_column=Column('paid', Numeric(10, 2), server_default=text('0')))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     payments: List['Payments'] = Relationship(back_populates='customers')
#     projects: List['Projects'] = Relationship(back_populates='customers')

#     class Config:
#         arbitrary_types_allowed = True  # Allow arbitrary types


# class Roles(SQLModel, table=True):
#     __table_args__ = (
#         PrimaryKeyConstraint('roleid', name='roles_pkey'),
#         UniqueConstraint('name', name='roles_name_key')
#     )

#     roleid: uuid.uuid.UUID = Field(sa_column=Column('roleid', Uuid, server_default=text('uuid_generate_v4()')))
#     name: str = Field(sa_column=Column('name', String(255), nullable=False))
#     description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     users: List['Users'] = Relationship(back_populates='roles')


# class Teams(SQLModel, table=True):
#     __table_args__ = (
#         PrimaryKeyConstraint('teamid', name='teams_pkey'),
#     )

#     teamid: uuid.uuid.UUID = Field(sa_column=Column('teamid', Uuid, server_default=text('uuid_generate_v4()')))
#     name: str = Field(sa_column=Column('name', String(255), nullable=False))
#     specialization: Optional[str] = Field(default=None, sa_column=Column('specialization', String(255)))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     projectteams: List['Projectteams'] = Relationship(back_populates='teams')


# class Vendors(SQLModel, table=True):
#     __table_args__ = (
#         PrimaryKeyConstraint('vendorid', name='vendors_pkey'),
#     )

#     vendorid: uuid.uuid.UUID = Field(sa_column=Column('vendorid', Uuid, server_default=text('uuid_generate_v4()')))
#     name: str = Field(sa_column=Column('name', String(255), nullable=False))
#     contactemail: Optional[str] = Field(default=None, sa_column=Column('contactemail', String(255)))
#     contactphone: Optional[str] = Field(default=None, sa_column=Column('contactphone', String(20)))
#     address: Optional[str] = Field(default=None, sa_column=Column('address', Text))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     materials: List['Materials'] = Relationship(back_populates='vendors')
#     vendorpayments: List['Vendorpayments'] = Relationship(back_populates='vendors')


# class Materials(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['vendorid'], ['vendors.vendorid'], name='materials_vendorid_fkey'),
#         PrimaryKeyConstraint('materialid', name='materials_pkey')
#     )

#     materialid: uuid.uuid.UUID = Field(sa_column=Column('materialid', Uuid, server_default=text('uuid_generate_v4()')))
#     name: str = Field(sa_column=Column('name', String(255), nullable=False))
#     vendorid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('vendorid', Uuid))
#     unitprice: Optional[Decimal] = Field(default=None, sa_column=Column('unitprice', Numeric(10, 2)))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     vendors: Optional['Vendors'] = Relationship(back_populates='materials')


# class Payments(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['customerid'], ['customers.customerid'], name='payments_customerid_fkey'),
#         PrimaryKeyConstraint('paymentid', name='payments_pkey')
#     )

#     paymentid: uuid.uuid.UUID = Field(sa_column=Column('paymentid', Uuid, server_default=text('uuid_generate_v4()')))
#     amount: Decimal = Field(sa_column=Column('amount', Numeric(10, 2), nullable=False))
#     paymentdate: date = Field(sa_column=Column('paymentdate', Date, nullable=False))
#     customerid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('customerid', Uuid))
#     paymentmethod: Optional[str] = Field(default=None, sa_column=Column('paymentmethod', String(255)))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     customers: Optional['Customers'] = Relationship(back_populates='payments')


# class Projects(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['customerid'], ['customers.customerid'], name='projects_customerid_fkey'),
#         PrimaryKeyConstraint('projectid', name='projects_pkey')
#     )

#     projectid: uuid.uuid.UUID = Field(sa_column=Column('projectid', Uuid, server_default=text('uuid_generate_v4()')))
#     name: str = Field(sa_column=Column('name', String(255), nullable=False))
#     description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
#     customerid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('customerid', Uuid))
#     sitelocation: Optional[str] = Field(default=None, sa_column=Column('sitelocation', Text))
#     budget: Optional[Decimal] = Field(default=None, sa_column=Column('budget', Numeric(15, 2)))
#     startdate: Optional[date] = Field(default=None, sa_column=Column('startdate', Date))
#     enddate: Optional[date] = Field(default=None, sa_column=Column('enddate', Date))
#     progress: Optional[str] = Field(default=None, sa_column=Column('progress', String(255)))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     customers: Optional['Customers'] = Relationship(back_populates='projects')
#     plans: List['Plans'] = Relationship(back_populates='projects')
#     projectpayments: List['Projectpayments'] = Relationship(back_populates='projects')
#     projectstatus: List['Projectstatus'] = Relationship(back_populates='projects')
#     projectteams: List['Projectteams'] = Relationship(back_populates='projects')
#     vendorpayments: List['Vendorpayments'] = Relationship(back_populates='projects')
#     empworklog: List['Empworklog'] = Relationship(back_populates='projects')


# class Users(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['roleid'], ['roles.roleid'], name='users_roleid_fkey'),
#         PrimaryKeyConstraint('userid', name='users_pkey'),
#         UniqueConstraint('email', name='users_email_key')
#     )

#     userid: uuid.uuid.UUID = Field(sa_column=Column('userid', Uuid, server_default=text('uuid_generate_v4()')))
#     firstname: str = Field(sa_column=Column('firstname', String(255), nullable=False))
#     lastname: str = Field(sa_column=Column('lastname', String(255), nullable=False))
#     email: str = Field(sa_column=Column('email', String(255), nullable=False))
#     password: str = Field(sa_column=Column('password', String(255), nullable=False))
#     roleid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('roleid', Uuid))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     roles: Optional['Roles'] = Relationship(back_populates='users')
#     employees: List['Employees'] = Relationship(back_populates='users')


# class Employees(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['userid'], ['users.userid'], name='employees_userid_fkey'),
#         PrimaryKeyConstraint('employeeid', name='employees_pkey'),
#         UniqueConstraint('email', name='employees_email_key')
#     )

#     employeeid: uuid.uuid.UUID = Field(sa_column=Column('employeeid', Uuid, server_default=text('uuid_generate_v4()')))
#     firstname: str = Field(sa_column=Column('firstname', String(255), nullable=False))
#     lastname: str = Field(sa_column=Column('lastname', String(255), nullable=False))
#     email: Optional[str] = Field(default=None, sa_column=Column('email', String(255)))
#     phonenumber: Optional[str] = Field(default=None, sa_column=Column('phonenumber', String(20)))
#     position: Optional[str] = Field(default=None, sa_column=Column('position', String(255)))
#     salary: Optional[Decimal] = Field(default=None, sa_column=Column('salary', Numeric(10, 2)))
#     advancegetamount: Optional[Decimal] = Field(default=None, sa_column=Column('advancegetamount', Numeric(10, 2), server_default=text('0')))
#     userid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('userid', Uuid))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     users: Optional['Users'] = Relationship(back_populates='employees')
#     empworklog: List['Empworklog'] = Relationship(back_populates='employees')


# class Plans(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='plans_projectid_fkey'),
#         PrimaryKeyConstraint('planid', name='plans_pkey')
#     )

#     planid: uuid.uuid.UUID = Field(sa_column=Column('planid', Uuid, server_default=text('uuid_generate_v4()')))
#     name: str = Field(sa_column=Column('name', String(255), nullable=False))
#     description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
#     projectid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
#     blueprint: Optional[str] = Field(default=None, sa_column=Column('blueprint', Text))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     projects: Optional['Projects'] = Relationship(back_populates='plans')


# class Projectpayments(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='projectpayments_projectid_fkey'),
#         PrimaryKeyConstraint('projectpaymentid', name='projectpayments_pkey')
#     )

#     projectpaymentid: uuid.uuid.UUID = Field(sa_column=Column('projectpaymentid', Uuid, server_default=text('uuid_generate_v4()')))
#     amount: Decimal = Field(sa_column=Column('amount', Numeric(10, 2), nullable=False))
#     paymentdate: date = Field(sa_column=Column('paymentdate', Date, nullable=False))
#     projectid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
#     paymentmethod: Optional[str] = Field(default=None, sa_column=Column('paymentmethod', String(255)))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     projects: Optional['Projects'] = Relationship(back_populates='projectpayments')


# class Projectstatus(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='projectstatus_projectid_fkey'),
#         PrimaryKeyConstraint('projectstatusid', name='projectstatus_pkey')
#     )

#     projectstatusid: uuid.uuid.UUID = Field(sa_column=Column('projectstatusid', Uuid, server_default=text('uuid_generate_v4()')))
#     status: str = Field(sa_column=Column('status', String(255), nullable=False))
#     projectid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
#     comments: Optional[str] = Field(default=None, sa_column=Column('comments', Text))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     projects: Optional['Projects'] = Relationship(back_populates='projectstatus')


# class Projectteams(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='projectteams_projectid_fkey'),
#         ForeignKeyConstraint(['teamid'], ['teams.teamid'], name='projectteams_teamid_fkey'),
#         PrimaryKeyConstraint('projectid', 'teamid', name='projectteams_pkey')
#     )

#     projectid: uuid.uuid.UUID = Field(sa_column=Column('projectid', Uuid, nullable=False))
#     teamid: uuid.uuid.UUID = Field(sa_column=Column('teamid', Uuid, nullable=False))
#     assigneddate: Optional[date] = Field(default=None, sa_column=Column('assigneddate', Date))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     projects: Optional['Projects'] = Relationship(back_populates='projectteams')
#     teams: Optional['Teams'] = Relationship(back_populates='projectteams')


# class Vendorpayments(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='vendorpayments_projectid_fkey'),
#         ForeignKeyConstraint(['vendorid'], ['vendors.vendorid'], name='vendorpayments_vendorid_fkey'),
#         PrimaryKeyConstraint('vendorpaymentid', name='vendorpayments_pkey')
#     )

#     vendorpaymentid: uuid.uuid.UUID = Field(sa_column=Column('vendorpaymentid', Uuid, server_default=text('uuid_generate_v4()')))
#     amount: Decimal = Field(sa_column=Column('amount', Numeric(10, 2), nullable=False))
#     paymentdate: date = Field(sa_column=Column('paymentdate', Date, nullable=False))
#     vendorid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('vendorid', Uuid))
#     projectid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
#     paymentmethod: Optional[str] = Field(default=None, sa_column=Column('paymentmethod', String(255)))
#     status: Optional[str] = Field(default=None, sa_column=Column('status', String(255), server_default=text("'Pending'::character varying")))
#     paidinadvance: Optional[Decimal] = Field(default=None, sa_column=Column('paidinadvance', Numeric(10, 2), server_default=text('0')))
#     balance: Optional[Decimal] = Field(default=None, sa_column=Column('balance', Numeric(10, 2), server_default=text('0')))
#     paid: Optional[Decimal] = Field(default=None, sa_column=Column('paid', Numeric(10, 2), server_default=text('0')))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     projects: Optional['Projects'] = Relationship(back_populates='vendorpayments')
#     vendors: Optional['Vendors'] = Relationship(back_populates='vendorpayments')


# class Empworklog(SQLModel, table=True):
#     __table_args__ = (
#         ForeignKeyConstraint(['employeeid'], ['employees.employeeid'], name='empworklog_employeeid_fkey'),
#         ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='empworklog_projectid_fkey'),
#         PrimaryKeyConstraint('worklogid', name='empworklog_pkey')
#     )

#     worklogid: uuid.uuid.UUID = Field(sa_column=Column('worklogid', Uuid, server_default=text('uuid_generate_v4()')))
#     workhours: int = Field(sa_column=Column('workhours', Integer, nullable=False))
#     workdate: date = Field(sa_column=Column('workdate', Date, nullable=False))
#     employeeid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('employeeid', Uuid))
#     projectid: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
#     taskdescription: Optional[str] = Field(default=None, sa_column=Column('taskdescription', Text))
#     createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     createdby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
#     updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
#     updatedby: Optional[uuid.uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
#     isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

#     employees: Optional['Employees'] = Relationship(back_populates='empworklog')
#     projects: Optional['Projects'] = Relationship(back_populates='empworklog')





from datetime import date, datetime
from decimal import Decimal
from typing import List, Optional
import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, Text, UniqueConstraint, Uuid, column, text
from sqlalchemy.orm.base import Mapped
from sqlmodel import Field, Relationship, SQLModel

class Customer(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('customerid', name='customer_pkey'),
    )

    customerid: uuid.UUID = Field(sa_column=Column('customerid', Uuid, server_default=text('gen_random_uuid()')))
    name: str = Field(sa_column=Column('name', String(100), nullable=False))
    email: Optional[str] = Field(default=None, sa_column=Column('email', String(100)))
    phone: Optional[str] = Field(default=None, sa_column=Column('phone', String(15)))
    address: Optional[str] = Field(default=None, sa_column=Column('address', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))

    projects: List['Projects'] = Relationship(back_populates='customer')
    payments: List['Payments'] = Relationship(back_populates='customer')


class Employee(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['roleid'], ['role.roleid'], name='employee_roleid_fkey'),
        ForeignKeyConstraint(['teamid'], ['team.teamid'], name='employee_teamid_fkey'),
        ForeignKeyConstraint(['userid'], ['users.userid'], name='employee_userid_fkey'),
        PrimaryKeyConstraint('employeeid', name='employee_pkey')
    )

    employeeid: uuid.UUID = Field(sa_column=Column('employeeid', Uuid, server_default=text('gen_random_uuid()')))
    fullname: str = Field(sa_column=Column('fullname', String(100), nullable=False))
    userid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('userid', Uuid))
    phonenumber: Optional[str] = Field(default=None, sa_column=Column('phonenumber', String(15)))
    email: Optional[str] = Field(default=None, sa_column=Column('email', String(100)))
    teamid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('teamid', Uuid))
    roleid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('roleid', Uuid))
    joineddate: Optional[date] = Field(default=None, sa_column=Column('joineddate', Date))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    designation: Optional[str] = Field(default=None, sa_column=Column('designation', String(100), nullable=True))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))

    role: Optional['Role'] = Relationship(back_populates='employee')
    team: Optional['Team'] = Relationship(back_populates='employee')
    users: Optional['Users'] = Relationship(back_populates='employee')
    team_: List['Team'] = Relationship(back_populates='employee_')


class Role(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('roleid', name='role_pkey'),
        UniqueConstraint('rolename', name='role_rolename_key')
    )

    roleid: uuid.UUID = Field(sa_column=Column('roleid', Uuid, server_default=text('gen_random_uuid()')))
    rolename: str = Field(sa_column=Column('rolename', String(50), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))
    

    employee: List['Employee'] = Relationship(back_populates='role')
    users: List['Users'] = Relationship(back_populates='role')


class Team(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['leademployeeid'], ['employee.employeeid'], name='fk_team_leademployee'),
        PrimaryKeyConstraint('teamid', name='team_pkey')
    )

    teamid: uuid.UUID = Field(sa_column=Column('teamid', Uuid, server_default=text('gen_random_uuid()')))
    teamname: str = Field(sa_column=Column('teamname', String(100), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
    leademployeeid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('leademployeeid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))

    employee: List['Employee'] = Relationship(back_populates='team')
    employee_: Optional['Employee'] = Relationship(back_populates='team_')
    projects: List['Projects'] = Relationship(back_populates='team')


class Vendor(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('vendorid', name='vendor_pkey'),
    )

    vendorid: uuid.UUID = Field(sa_column=Column('vendorid', Uuid, server_default=text('gen_random_uuid()')))
    name: str = Field(sa_column=Column('name', String(100), nullable=False))
    email: Optional[str] = Field(default=None, sa_column=Column('email', String(100)))
    phone: Optional[str] = Field(default=None, sa_column=Column('phone', String(15)))
    address: Optional[str] = Field(default=None, sa_column=Column('address', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))

    materials: List['Materials'] = Relationship(back_populates='vendor')
    payments: List['Payments'] = Relationship(back_populates='vendor')


class Projects(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['customer.customerid'], name='projects_customerid_fkey'),
        ForeignKeyConstraint(['teamid'], ['team.teamid'], name='projects_teamid_fkey'),
        PrimaryKeyConstraint('projectid', name='projects_pkey')
    )

    projectid: uuid.UUID = Field(sa_column=Column('projectid', Uuid, server_default=text('gen_random_uuid()')))
    name: str = Field(sa_column=Column('name', String(100), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
    customerid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('customerid', Uuid))
    teamid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('teamid', Uuid))
    startdate: Optional[date] = Field(default=None, sa_column=Column('startdate', Date))
    enddate: Optional[date] = Field(default=None, sa_column=Column('enddate', Date))
    status: Optional[str] = Field(default=None, sa_column=Column('status', String(50)))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))

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

    userid: uuid.UUID = Field(sa_column=Column('userid', Uuid, server_default=text('gen_random_uuid()')))
    username: str = Field(sa_column=Column('username', String(50), nullable=False))
    email: str = Field(sa_column=Column('email', String(100), nullable=False))
    password: str = Field(sa_column=Column('password', String(100), nullable=False))
    passwordhash: str = Field(sa_column=Column('passwordhash', Text, nullable=True))
    roleid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('roleid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))
    phonenumber: Optional[str] = Field(default=None, sa_column=Column('phonenumber', String(15)))
    usertype: Optional[str] = Field(default=None, sa_column=Column('usertype', String(50)))
    isactive: Optional[bool] = Field(default=None, sa_column=Column('isactive', Boolean, server_default=text('true')))
    

    employee: List['Employee'] = Relationship(back_populates='users')
    role: Optional['Role'] = Relationship(back_populates='users')


class Materials(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='materials_projectid_fkey'),
        ForeignKeyConstraint(['vendorid'], ['vendor.vendorid'], name='materials_vendorid_fkey'),
        PrimaryKeyConstraint('materialid', name='materials_pkey')
    )

    materialid: uuid.UUID = Field(sa_column=Column('materialid', Uuid, server_default=text('gen_random_uuid()')))
    name: str = Field(sa_column=Column('name', String(100), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column('description', Text))
    quantity: Optional[int] = Field(default=None, sa_column=Column('quantity', Integer, server_default=text('0')))
    unitprice: Optional[Decimal] = Field(default=None, sa_column=Column('unitprice', Numeric(10, 2)))
    vendorid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('vendorid', Uuid))
    projectid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))

    projects: Optional['Projects'] = Relationship(back_populates='materials')
    vendor: Optional['Vendor'] = Relationship(back_populates='materials')


class Payments(SQLModel, table=True):
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['customer.customerid'], name='payments_customerid_fkey'),
        ForeignKeyConstraint(['projectid'], ['projects.projectid'], name='payments_projectid_fkey'),
        ForeignKeyConstraint(['vendorid'], ['vendor.vendorid'], name='payments_vendorid_fkey'),
        PrimaryKeyConstraint('paymentid', name='payments_pkey')
    )

    paymentid: uuid.UUID = Field(sa_column=Column('paymentid', Uuid, server_default=text('gen_random_uuid()')))
    amount: Decimal = Field(sa_column=Column('amount', Numeric(12, 2), nullable=False))
    paymentdate: date = Field(sa_column=Column('paymentdate', Date, nullable=False))
    paymenttype: Optional[str] = Field(default=None, sa_column=Column('paymenttype', String(50)))
    customerid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('customerid', Uuid))
    vendorid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('vendorid', Uuid))
    projectid: Optional[uuid.UUID] = Field(default=None, sa_column=Column('projectid', Uuid))
    remarks: Optional[str] = Field(default=None, sa_column=Column('remarks', Text))
    createddate: Optional[datetime] = Field(default=None, sa_column=Column('createddate', DateTime, server_default=text('CURRENT_TIMESTAMP')))
    createdby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('createdby', Uuid))
    updateddate: Optional[datetime] = Field(default=None, sa_column=Column('updateddate', DateTime))
    updatedby: Optional[uuid.UUID] = Field(default=None, sa_column=Column('updatedby', Uuid))

    customer: Optional['Customer'] = Relationship(back_populates='payments')
    projects: Optional['Projects'] = Relationship(back_populates='payments')
    vendor: Optional['Vendor'] = Relationship(back_populates='payments')

