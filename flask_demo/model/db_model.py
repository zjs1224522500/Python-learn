from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/students'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, server_default='', unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

    def to_json(self):
        return {
                'id': self.id,
                'name': self.name
                }


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)
    role_id = db.Column(db.Integer, nullable=False, server_default='0')

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    # def __repr__(self):
    #     return '<User %r,Role id %r>' % (self.username, self.role_id)

    def to_json(self):
        return {
                'id': self.id,
                'username': self.username
                }
