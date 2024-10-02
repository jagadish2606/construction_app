# from typing import Optional
# from fastapi import Query
# from fastapi.params import Depends
# from Sqlalchemy import Select
# from sqlmodel import Session, select, func
# from core.database.db import get_db
# from core.utils.middewares import request_object


# class Paginator:
#     def __init__(self, db: Session, query: Select, page: int, per_page: int):
#         self.db = db
#         self.query = query
#         self.page = page
#         self.per_page = per_page
#         self.limit = per_page
#         self.offset = (page - 1) * per_page
#         self.request = request_object.get()
#         self.number_of_pages = 0
#         self.next_page = ''
#         self.previous_page = ''
        
    
#     def _get_next_page(self) -> Optional[str]:
#         if self.page >= self.number_of_pages:
#             return
        
#         url = self.request.url.include_query_params(page=self.page + 1)
#         return str(url)
    
    
#     def _get_previous_page(self) -> Optional[str]:
#         if self.page == 1 or self.page > self.number_of_pages + 1:
#             return
#         url = self.request.url.include_query_params(page=self.page - 1)
#         return str(url)
    
#     def get_response(self) -> dict:
#         return {
#             'count': self._get_total_count(),
#             'next_page': self._get_next_page(),
#             'pervious_page': self._get_previous_page(),
#             'items': [item for item in self.db.exec(self.query.offset(self.offset).limit(self.limit))]
#         }
        
#     def _get_number_of_pages(self, count: int) -> int:
#         rest = count % self.per_page
#         quotient = count // self.per_page
#         return quotient if not rest else quotient + 1
    
#     def _get_total_count(self) -> int:
#         count = self.db.scalar(select(func.count()).select_from(self.query.subquery()))
#         self.number_of_pages = self._get_number_of_pages(count)
#         return count
    
#     def paginate(query: select, page: int, per_page: int,
#                  db. Session = Depends(get_db)) -> dict:
        
#         Paginator = Paginator(db, query, page, per_page)
#         return Paginator.get_respone()
    
# class PaginatedParams:
#     def __init__(self, page: int = Query(1, ge=1), per_page: int = Query(100, ge=0)):
#         self.page = page
#         self.per_page = per_page

from typing import Optional
from fastapi import Query, Depends
from sqlalchemy import Select, func  # Use sqlalchemy.func instead of sqlmodel.func
from sqlmodel import Session, select  # Use sqlmodel's select for query building
from construction_app.core.database.db import get_db
from construction_app.core.utils.middlewares import request_object  # Fixed typo in 'middlewares'


class Paginator:
    def __init__(self, db: Session, query: Select, page: int, per_page: int):
        self.db = db
        self.query = query
        self.page = page
        self.per_page = per_page
        self.limit = per_page
        self.offset = (page - 1) * per_page
        self.request = request_object.get()
        self.number_of_pages = 0
        self.next_page = ''
        self.previous_page = ''

    def _get_next_page(self) -> Optional[str]:
        if self.page >= self.number_of_pages:
            return None
        url = self.request.url.include_query_params(page=self.page + 1)
        return str(url)

    def _get_previous_page(self) -> Optional[str]:
        if self.page == 1 or self.page > self.number_of_pages + 1:
            return None
        url = self.request.url.include_query_params(page=self.page - 1)
        return str(url)

    def get_response(self) -> dict:
        return {
            'count': self._get_total_count(),
            'next_page': self._get_next_page(),
            'previous_page': self._get_previous_page(),
            'items': [item for item in self.db.exec(self.query.offset(self.offset).limit(self.limit))]
        }

    def _get_number_of_pages(self, count: int) -> int:
        rest = count % self.per_page
        quotient = count // self.per_page
        return quotient if not rest else quotient + 1

    def _get_total_count(self) -> int:
        count = self.db.scalar(select(func.count()).select_from(self.query.subquery()))
        self.number_of_pages = self._get_number_of_pages(count)
        return count

    # @staticmethod
def paginate(query: Select, page: int, per_page: int, db: Session = Depends(get_db)) -> dict:
        paginator = Paginator(db, query, page, per_page)  # Fixed capitalization of 'Paginator'
        return paginator.get_response()  # Fixed typo 'get_respone'


class PaginatedParams:
    def __init__(self, page: int = Query(1, ge=1), per_page: int = Query(100, ge=0)):
        self.page = page
        self.per_page = per_page
