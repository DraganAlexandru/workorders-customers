from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import WorkOrder, Customer


@convert_kwargs_to_snake_case
def resolve_create_work_order(_, info, type, schedule, customer_id):
    customer = Customer.query.get(customer_id)

    if customer is None:
        raise ValueError(f'Customer with id {customer_id} not found.')

    work_order = WorkOrder(
        type=type,
        schedule=schedule,
        customer=customer
    )
    db.session.add(work_order)
    db.session.commit()

    return work_order


@convert_kwargs_to_snake_case
def resolve_create_customer(_, info, first_name, last_name, address, email, phone_number):
    customer = Customer(
        first_name=first_name,
        last_name=last_name,
        address=address,
        email=email,
        phone_number=phone_number
    )
    db.session.add(customer)
    db.session.commit()

    return customer
