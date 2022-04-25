from tortoise import Model, fields


class UserModel(Model):
    id: int = fields.BigIntField(pk=True)
    access_token: str = fields.TextField()
    refresh_token: str = fields.TextField()

