from pydantic import BaseModel

class Tour(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    disponible: bool
