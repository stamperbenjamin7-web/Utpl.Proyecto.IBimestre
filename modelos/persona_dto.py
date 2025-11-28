from pydantic import BModel, EmailStr, Field, model_validator

class Persona(BaseModel):
    nombre: str = Field(..., min_length=4, max_length=100, description="Nombre de la persona")
    apellido: str = Field(..., min_length=4, max_length=100, description="Apellido de la persona")
    email: EmailStr = Field(..., description="Correo electrónico de la persona")
    edad: int = Field(..., ge=10, le=120, description="Edad de la persona")
    direccion: str = Field(..., min_length=10, max_length=200, description="Dirección de la persona")
    telefono: str = Field(..., min_length=7, max_length=15, description="Número de teléfono de la persona")
    identificacion: str = Field(..., min_length=5, max_length=20, description="Identificación de la persona")

    