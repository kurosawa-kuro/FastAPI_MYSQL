# -*- encoding: utf-8 -*-
import datetime
import uuid
import sys
from sqlalchemy import (Column, String, Text, ForeignKey, CHAR, VARCHAR, INT,
                        create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index,
                        and_)
from sqlalchemy.ext.declarative import declarative_base

sys.dont_write_bytecode = True

base = declarative_base()


class user(base):
    __tablename__ = 'User'
    id = Column(CHAR(36), primary_key=True)
    name = Column(VARCHAR(255))
    email = Column(VARCHAR(255))

    def __init__(self):
        self.id = str(uuid.uuid4())
        now_data_time = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        self.create_date_time = now_data_time
        self.update_date_time = now_data_time
