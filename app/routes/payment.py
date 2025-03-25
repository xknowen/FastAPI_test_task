from sanic import Blueprint
from sanic.response import json


account_bp = Blueprint("account")


@account_bp.get("/accounts")
async def get_accounts(request):
    return json({"message": "User accounts list will be implemented here"})