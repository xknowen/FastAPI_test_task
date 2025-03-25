from sanic import Blueprint
from sanic.response import json


user_bp = Blueprint("user")


@user_bp.get("/me")
async def get_user_info(request):
    return json({"message": "User info will be implemented here"})