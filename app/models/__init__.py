from app import db, lm
from flask_login import UserMixin


@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'table_users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.username


class Routers(db.Model):
    __tablename__ = 'table_routers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String, nullable=False)
    ip_address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.hostname, self.ip_address


class Switches(db.Model):
    __tablename__ = 'table_switches'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String, nullable=False)
    ip_address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.hostname, self.ip_address


class Olts(db.Model):
    __tablename__ = 'table_olts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String, nullable=False)
    ip_address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.hostname, self.ip_address


class NeighborBgpIpv6(db.Model):
    __tablename__ = 'neighbor_bgp_ipv6'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)
    neighbor = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.description


class NeighborBgpIpv4(db.Model):
    __tablename__ = 'neighbor_bgp_ipv4'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)
    neighbor = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.description
