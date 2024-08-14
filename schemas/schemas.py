from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Int(required=True)

class StoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    items = fields.List(fields.Nested(ItemSchema))

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True)
    sdt = fields.Str(required=True)
    is_active = fields.Bool(required=False, default=True)
    id_role = fields.Int(required=False, default=2)

class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    is_active = fields.Bool(required=True, default=True)

class LoginSchema(Schema):
    sdt = fields.Str(required=True)
    password = fields.Str(required=True)
