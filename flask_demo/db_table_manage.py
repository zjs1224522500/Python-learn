import sys
from os import path
from flask_demo.model.db_model import db, User, Role

ROOT = path.realpath(path.join(path.dirname(__file__), "../.."))
sys.path.append(ROOT)


def create_tables():
    db.create_all()


def drop_tables():
    db.drop_all()


def insert_role_example_data():
    db.session.add(Role(name='Admin'))
    db.session.commit()
    db.session.add(Role(name='Moderator'))
    db.session.add(Role(name='User'))
    db.session.commit()


def insert_user_example_date():
    db.session.add_all(
        [User(username='john', role_id=1), User(username='susan', role_id=3), User(username='david', role_id=3)])
    db.session.commit()


if __name__ == '__main__':
    # create_tables()
    # drop_tables()
    # insert_role_example_data()
    insert_user_example_date()
