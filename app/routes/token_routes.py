from fastapi import APIRouter,Header, HTTPException
from controllers.token_controller import *
from models.token_model import Auth
from controllers.google_auth import login_google_user
from fastapi.responses import RedirectResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from controllers.google_auth import login_google_user, exchange_code_for_token
from fastapi import Query, HTTPException


router = APIRouter()

nuevo_auth = AuthController()


@router.post("/token")
async def token(auth: Auth):
    
    ##print("AQUI")
    user = nuevo_auth.login(auth)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    else:
        print(user)
        access_token = nuevo_auth.create_access_token(user)
    return access_token


@router.post("/verifytoken")
def verifytoken(Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=400, detail="Authorization header is missing")

    parts = Authorization.split(" ")
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(status_code=400, detail="Invalid Authorization header format")

    token = parts[1]
    print(token)

    return nuevo_auth.validate_token(token)

@router.post("/token/google")
async def token_google(code: str = Query(...)):
    """Recibe un código de Google y devuelve un JWT válido para la API"""
    try:
        # Primero, intercambiar el código por el token de acceso
        access_token_data = exchange_code_for_token(code, "http://localhost:8000/token/google/callback")
        access_token = access_token_data.get("access_token")
        
        # Luego, genera el token JWT usando el acceso de Google
        jwt_token = login_google_user(access_token)
        
        # Redirige a la página de éxito con el JWT token
        confirmation_url = f"http://localhost:8000/auth/success?token={jwt_token}"
        return RedirectResponse(url=confirmation_url)

    except Exception as e:
        # En caso de error, redirige a la página de error
        error_url = f"http://localhost:8000/auth/error?message={str(e)}"
        return RedirectResponse(url=error_url)
    
@router.get("/auth/success")
async def success_page(request: Request, token: str):
    # Puedes hacer algo con el token si es necesario
    return HTMLResponse(content=f"<h1>Inicio de sesión exitoso</h1><p>Tu token JWT: {token}</p>")

@router.get("/auth/error")
async def error_page(request: Request, message: str):
    return HTMLResponse(content=f"<h1>Error</h1><p>{message}</p>")

