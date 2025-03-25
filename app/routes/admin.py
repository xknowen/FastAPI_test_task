from sanic import Blueprint
from sanic.response import json


admin_bp = Blueprint("admin")


@admin_bp.get("/users")
async def get_users(request):
    return json({"message": "Admin users list will be implemented here"})
