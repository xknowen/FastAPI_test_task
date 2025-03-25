from sanic import Blueprint, Sanic
from sanic.response import json
from sanic_jwt import Initialize

app = Sanic('MyApp')
auth_bp = Blueprint("auth")


async def authenticate(request, *args, **kwargs):
    return json({"message": "Auth logic will be implemented here"})


Initialize(app, authenticate=authenticate)

