from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Number(min=1, max=1000)
    store_id = fields.Str(required=True)