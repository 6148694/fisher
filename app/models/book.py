# -*- coding: utf-8 -*-
"""
Create Time: 2021/6/21 7:25 下午
Author: Aries
"""
#flask sqlAlchemy
from sqlalchemy import Column,Integer,String
class Book():
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    author = Column(String(30),default="佚名")
    binding = Column(String(28))