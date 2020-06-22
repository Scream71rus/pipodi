
from models.base_model import BaseModel

CREATE_SCHEMA = {
    "email": {"type": "numeral", "required": True, "nullable": False},
    "password": {"type": "string", "required": True, "empty": False, "nullable": False},
    "name": {"type": "string", "nullable": True},
    "phone": {"type": "numeral", "nullable": True},
    "service": {"type": "list", "nullable": True},
    "confirm_email": {"type": "list", "nullable": True},
}

UPDATE_SCHEMA = {
    "id": {"type": "numeral", "required": True, "nullable": False},
    "email": {"type": "numeral", "required": True, "nullable": False},
    "password": {"type": "string", "required": True, "empty": False, "nullable": False},
    "name": {"type": "string", "nullable": True},
    "phone": {"type": "numeral", "nullable": True},
    "service": {"type": "boolean", "required": True, "nullable": False},
    "confirm_email": {"type": "boolean", "required": True, "nullable": False},
    "created": {"type": "list", "nullable": True},
}


class CustomerModel(BaseModel):
    @classmethod
    async def get_by_email(cls, email):
        sql = "select * from pipodi.customer where email = $1"
        cursor = await cls.db.fetchrow(sql, email)
        return cursor

    @classmethod
    async def create(cls, email, password):
        sql = "insert into pipodi.customer(email, password) values($1, $2) returning id"
        cursor = await cls.db.execute(sql, email, password)
        return cursor
