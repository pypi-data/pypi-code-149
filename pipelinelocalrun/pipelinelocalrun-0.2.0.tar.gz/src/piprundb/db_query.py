from sqlalchemy.sql import or_
from pipruncommon import IndexEntitiesRequest

class Operator():
    EQUAL = "eq"
    NOT_EQUAL = "ne"
    GREATER_THAN = "gt"
    LESS_THAN = "lt"
    GREATER_OR_EQUAL = 'ge'
    LESS_OR_EQUAL = 'le'
    EXISTS = "exists"
    CONTAINS = "contains"
    STARTSWITH = "startswith"

class Order():
    ASC = "Asc"
    DESC = "Desc"

def build_query_list(cls, index_entities_request:IndexEntitiesRequest, session) -> list:
    filters_list = index_entities_request.filters
    query_list = []
    for filter in filters_list:
        field = getattr(cls, filter.field)
        if(filter.operator == Operator.EQUAL):
            query_list.append(field == filter.values[0])
        elif(filter.operator == Operator.NOT_EQUAL):
            query_list.append(field.not_in(filter.values))
        elif(filter.operator == Operator.GREATER_THAN):
            query_list.append(field > filter.values[0])
        elif(filter.operator == Operator.LESS_THAN):
            query_list.append(field < filter.values[0])
        elif(filter.operator == Operator.GREATER_OR_EQUAL):
            query_list.append(field >= filter.values[0])
        elif(filter.operator == Operator.LESS_OR_EQUAL):
            query_list.append(field <= filter.values[0])
        elif(filter.operator == Operator.EXISTS):
            query_list.append(field.in_(filter.values))
        elif(filter.operator == Operator.CONTAINS):     # case insensitive
            query_list.append(or_(field.contains(i) for i in filter.values))
            # query_list.append(or_(field.like("%" + i + "%") for i in filter.values))  # this is ok
        elif(filter.operator == Operator.STARTSWITH):   # case insensitive
            query_list.append(or_(field.startswith(i) for i in filter.values))
            # query_list.append(or_(field.like(i + "%") for i in filter.values))    # this is ok
    return query_list

def query(cls, index_entities_request:IndexEntitiesRequest, session) -> list:
    query_list = build_query_list(cls, index_entities_request, session)
    order_list = index_entities_request.order
    pageSize = index_entities_request.pageSize
    skip = index_entities_request.skip
    order_by_list = []
    if order_list is not None:
        for order in order_list:
            field = getattr(cls, order.field)
            if(order.direction == Order.ASC):
                order_by_list.append(field.asc())
            if(order.direction == Order.DESC):
                order_by_list.append(field.desc())
    if skip is None:
        skip = 0
    if pageSize is None:
        result_list = session.query(cls).filter(*query_list).order_by(*order_by_list).offset(skip).all()
    else:
        result_list = session.query(cls).filter(*query_list).order_by(*order_by_list).limit(pageSize).offset(skip).all()
    return result_list

def query_count(cls, index_entities_request:IndexEntitiesRequest, session) -> int:
    skip = index_entities_request.skip
    query_list = build_query_list(cls, index_entities_request, session)
    if skip is None:
        skip = 0
    count = session.query(cls).filter(*query_list).offset(skip).count()
    return count