"""
API REST básica con FastAPI
Este es un esqueleto de API para enseñar a estudiantes
"""

from fastapi import FastAPI, HTTPException
from modelos.persona_dto import Persona

dbPersona = []

# Crear la instancia de FastAPI
app = FastAPI(
    title="API de Ejemplo UTPL - fdquinones@utpl.edu.ec",
    description="API REST básica para aprender FastAPI en Interoperabilidad de Sistemas",
    version="1.0.0"
)


@app.get("/")
def root():
    """
    Endpoint raíz - Hola Mundo
    """
    return {"mensaje": "¡Hola Mundo desde FastAPI por Felipe!"}


@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    """
    Endpoint de ejemplo con parámetro de ruta
    """
    return {"mensaje": f"¡Hola {nombre}! Bienvenido a la API"}


@app.get("/info")
def informacion():
    """
    Endpoint de información de la API
    """
    return {
        "nombre": "API de Ejemplo UTPL",
        "version": "1.0.0",
        "descripcion": "Esta es una API básica creada con FastAPI para propósitos educativos"
    }
    
@app.post("/personas", response_model=Persona, tags=["Personas"])
def crear_persona(persona: Persona):
    """
    Endpoint para crear una nueva persona
    """
    dbPersona.append(persona)
    return persona

@app.get("/personas", response_model=list[Persona], tags=["Personas"])
def obtener_personas():
    """
    Endpoint para crear una nueva persona
    """
    return dbPersona


@app.get("/personas/{identificacion}", response_model=Persona, tags=["Personas"])
def obtener_persona_por_identificacion(identificacion: str):
    """Buscar una persona por su identificación."""
    for persona in dbPersona:
        if persona.identificacion == identificacion:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")


@app.put("/personas/{identificacion}", response_model=Persona, tags=["Personas"])
def actualizar_persona(identificacion: str, persona_actualizada: Persona):
    """Actualizar una persona existente por su identificación.

    La identificación de la ruta debe coincidir con la del cuerpo.
    """
    if persona_actualizada.identificacion != identificacion:
        raise HTTPException(status_code=400, detail="La identificación del cuerpo no coincide con la ruta")

    for idx, persona in enumerate(dbPersona):
        if persona.identificacion == identificacion:
            dbPersona[idx] = persona_actualizada
            return persona_actualizada
    raise HTTPException(status_code=404, detail="Persona no encontrada")


@app.delete("/personas/{identificacion}", response_model=Persona, tags=["Personas"])
def eliminar_persona(identificacion: str):
    """Eliminar una persona por su identificación.

    Retorna la persona eliminada o 404 si no existe.
    """
    for idx, persona in enumerate(dbPersona):
        if persona.identificacion == identificacion:
            # Remover y retornar la persona eliminada
            return dbPersona.pop(idx)
    raise HTTPException(status_code=404, detail="Persona no encontrada")

