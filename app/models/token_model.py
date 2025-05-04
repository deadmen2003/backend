from pydantic import BaseModel

class Auth(BaseModel):
    id: int = None
    usuario: str
    password: str