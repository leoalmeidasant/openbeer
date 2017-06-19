from marshmallow import Schema, fields

class SellSchema(Schema):
    name = fields.Str()
    y = fields.Int()
