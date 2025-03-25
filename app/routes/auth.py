from sanic import Blueprint
from sanic.response import json
from sanic_jwt import Initialize

auth_bp = Blueprint("auth")


async def authenticate(request, *args, **kwargs):
    return json({"message": "Auth logic will be implemented here"})


Initialize(auth_bp, authenticate=authenticate)
