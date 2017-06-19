from marshmallow import Schema, fields

class WeekdaySchema(Schema):
    dias = fields.Int()
    marca = fields.Str()
    quanitidade = fields.Int()
