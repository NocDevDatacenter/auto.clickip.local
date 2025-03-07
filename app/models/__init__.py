from app import db, lm
from flask_login import UserMixin


@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.username


class Routers(db.Model):
    __tablename__ = 'routers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String, nullable=False)
    ip_address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.hostname, self.ip_address


class Switches(db.Model):
    __tablename__ = 'switches'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String, nullable=False)
    ip_address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.hostname, self.ip_address


class Olts(db.Model):
    __tablename__ = 'olts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String, nullable=False)
    ip_address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.hostname, self.ip_address


class BgpNeighbor(db.Model):
    __tablename__ = 'bgp_neighbors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)
    neighbor = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.description
