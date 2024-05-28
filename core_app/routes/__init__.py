from core_app.routes.user.blueprint import user_api, user_blueprint
from core_app.routes.health_check.blueprint import health_api, health_blueprint

blueprints = [
    user_blueprint,
    health_blueprint,
]

apis = [
    user_api,
    health_api,
]