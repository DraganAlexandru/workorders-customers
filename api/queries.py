from ariadne import convert_kwargs_to_snake_case

from .models import WorkOrder


def resolve_work_orders(obj, info):
    return [workOrder.to_dict() for workOrder in WorkOrder.query.all()]


@convert_kwargs_to_snake_case
def resolve_work_order(obj, info, work_order_id):
    return WorkOrder.query.get(work_order_id)
