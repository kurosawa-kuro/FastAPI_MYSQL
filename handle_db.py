# -*- encoding: utf-8 -*-
import sys
import models
import databases
import datetime

sys.dont_write_bytecode = True


def select_all_user():
    session = databases.create_new_session()
    user_list = session.query(models.user).\
        all()
    if user_list == None:
        user_list = []
    return user_list


def create_user(name, email, password):
    session = databases.create_new_session()
    user = models.user()

    user.name = name
    user.email = email
    user.password = password
    user.createdAt = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    user.updatedAt = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

    session.add(user)
    session.commit()

    return 0


def select_user(user_id):
    session = databases.create_new_session()
    user = session.query(models.user).\
        filter(models.user.id == user_id).\
        first()
    if user == None:
        user = ""
    return user


def update_user(user_id, name, email, user_status):
    session = databases.create_new_session()
    user = session.query(models.user).\
        filter(models.user.id == user_id).\
        first()
    if user == None:
        return 1
    user.name = name
    user.mail_address = email
    user.status = user_status
    session.commit()
    return 0


def delete_user(user_id):
    session = databases.create_new_session()
    user = session.query(models.user).\
        filter(models.user.id == user_id).\
        first()
    if user == None:
        return 1
    user.status = "deleted"
    session.commit()
    return 0
