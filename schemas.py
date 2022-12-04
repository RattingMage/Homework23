from marshmallow import fields, Schema, validates_schema, ValidationError


class ParamsSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        valid_cmd_commands = {'filter', 'sort', 'map', 'limit', 'unique'}

        if values['cmd'] not in valid_cmd_commands:
            raise ValidationError({"cmd": f"Invalid command={values['cmd']}"})

        return values


class ParamsListSchema(Schema):
    queries = fields.Nested(ParamsSchema, many=True)
