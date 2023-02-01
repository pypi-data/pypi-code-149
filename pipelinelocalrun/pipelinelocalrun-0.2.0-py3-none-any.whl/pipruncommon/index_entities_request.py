from marshmallow import Schema, fields, post_load, EXCLUDE

class IndexEntitiesRequestFilter ():
    def __init__(
        self,
        field: str,
        operator: str,
        values: list,
        ):
        self.field = field
        self.operator = operator
        self.values = values

class IndexEntitiesRequestFilterSchema(Schema):
    field = fields.Str()
    operator = fields.Str()
    # values = fields.List(fields.Str(allow_none = True), many = True)
    values = fields.List(fields.Raw(allow_none = True), many = True)

    @post_load
    def make_user(self, data, **kwargs):
        return IndexEntitiesRequestFilter(**data)

class IndexEntitiesRequestOrder():
    def __init__(
        self,
        field: str,
        direction: str,
        ):
        self.field = field
        self.direction  = direction   

class IndexEntitiesRequestOrderSchema(Schema):
    field = fields.Str()
    direction = fields.Str()

    @post_load
    def make_user(self, data, **kwargs):
        return IndexEntitiesRequestOrder(**data)  

class IndexEntitiesRequest():
    def __init__(
        self,
        filters: list = None,
        order: list = None,
        pageSize: int = None,
        skip: int = None,
        includeTotalResultCount: bool = None,
        ):
        self.filters = filters
        self.order = order
        self.pageSize = pageSize
        self.skip = skip
        self.includeTotalResultCount = includeTotalResultCount 

class IndexEntitiesRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    filters = fields.Nested(IndexEntitiesRequestFilterSchema, many = True) # if field nested object is a list, we should make many = True
    order = fields.Nested(IndexEntitiesRequestOrderSchema, many = True)
    pageSize = fields.Int()
    skip = fields.Int()
    includeTotalResultCount = fields.Boolean()

    @post_load      # Register a method to invoke after deserializing an object.
    def make_user(self, data, **kwargs):
        return IndexEntitiesRequest(**data)