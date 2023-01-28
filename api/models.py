from enum import Enum

from sqlalchemy.orm import backref

from api import db


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    address = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "email": self.email,
            "phone_number": self.phone_number,
        }


class AllowedType(Enum):
    Install = "Install"
    Service = "Service"


class WorkOrder(db.Model):
    __tablename__ = 'workOrder'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(AllowedType))
    schedule = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship("Customer", backref=backref("customer", uselist=False))

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "schedule": self.schedule,
            "customer": self.customer
        }
