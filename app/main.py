from fastapi import FastAPI
from app.routes.token_routes import router as token_router
from app.routes.user_routes import router as user_router
from app.routes.comunidad_routes import router as comunidad_router
from app.routes.contacto_routes import router as contacto_router
from app.routes.amistades_routes import router as amistades_router
from app.routes.atributo_routes import router as atributo_router
from app.routes.atributo_usuario_routes import router as atributo_usuario_router
from app.routes.comentario_routes import router as comentario_router
from app.routes.post_routes import router as post_router
from app.routes.role_routes import router as role_router
from app.routes.bitacora_routes import router as bitacora_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",  # Permitir Angular
    "http://127.0.0.1:4200",  # Permitir FastAPI en local
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todas las cabeceras
)


app.include_router(token_router)
app.include_router(user_router)
app.include_router(comunidad_router)
app.include_router(contacto_router)
app.include_router(amistades_router)
app.include_router(atributo_router)
app.include_router(atributo_usuario_router)
app.include_router(comentario_router)
app.include_router(post_router)
app.include_router(role_router)
app.include_router(bitacora_router)

# Imprime las rutas disponibles
@app.on_event("startup")
def print_routes():
    print("Rutas disponibles:")
    for route in app.routes:
        print(route.path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)