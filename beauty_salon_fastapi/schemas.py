from pydantic import BaseModel


class CreateUsers(BaseModel):

    name: str
    num_tel: int

# class FormData(BaseModel):
#     username: str = None
#     num_tel: int