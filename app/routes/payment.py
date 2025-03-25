from sanic import Blueprint, response


payment_bp = Blueprint("payment")


@payment_bp.post("/create")
async def create_payment(request):
    return response.json({"message": "Платеж создан"}, status=201)
