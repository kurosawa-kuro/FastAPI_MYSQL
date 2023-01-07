# -*- encoding: utf-8 -*-
import datetime
import uuid
import sys
from sqlalchemy import (Column, String, Text, ForeignKey, CHAR, VARCHAR, INT,
                        create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index,
                        and_, INTEGER)
from sqlalchemy.ext.declarative import declarative_base

sys.dont_write_bytecode = True

base = declarative_base()


class user(base):
    __tablename__ = 'User'
    id = Column('id',
                INTEGER(),
                primary_key=True,
                autoincrement=True,)
    name = Column(VARCHAR(255))
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(255))
    createdAt = DATETIME()
    updatedAt = DATETIME()

    def __init__(self):
        # self.id = str(uuid.uuid4())
        now_data_time = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        self.createdAt = now_data_time
        self.updatedAt = now_data_time
