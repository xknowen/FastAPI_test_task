from sanic import Sanic
from sanic.response import json
from core.database import engine
from models.base import Base
from routes.auth import auth_bp
from routes.user import user_bp
from routes.admin import admin_bp
from routes.account import account_bp
from routes.payment import payment_bp


app = Sanic("TestTaskSanic")


@app.listener("before_server_start")
async def setup_db(app, loop):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.blueprint(auth_bp)
app.blueprint(user_bp)
app.blueprint(admin_bp)
app.blueprint(account_bp)
app.blueprint(payment_bp)


@app.get("/")
async def index(request):
    return json({"message": "Hello, Sanic!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
