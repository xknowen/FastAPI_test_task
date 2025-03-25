from sanic import Blueprint
from sanic.response import json


payment_bp = Blueprint("payment")


@payment_bp.get("/accounts")
async def get_accounts(request):
    return json({"message": "Payment logic will be implemented here"})