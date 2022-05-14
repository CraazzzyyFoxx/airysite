from datetime import datetime

from tortoise import Model, fields


class UserModel(Model):
    id: int = fields.BigIntField(pk=True)
    access_token: str = fields.TextField()
    access_token_expires: datetime = fields.DatetimeField()
    refresh_token: str = fields.TextField()

    class Meta:
        """Metaclass to set table name and description"""

        table = "users"
        table_description = "Stores information about the users and his Oauth2 tokens"
