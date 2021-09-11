from marshmallow import Schema, fields, validate

class SearchTextInput(Schema):
    
    file_name = fields.String(required=True,)
    position = fields.List(fields.Integer, required=True, validate=validate.Length(equal=4))