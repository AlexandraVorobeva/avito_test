from pydantic import BaseModel


class _BaseContact(BaseModel):
    first_name: str
    last_name: str
    email: str



class Contact(_BaseContact):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class CreateContact(_BaseContact):
    pass