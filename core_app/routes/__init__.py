from core_app.routes.health_check.blueprint import health_api, health_blueprint
from core_app.routes.user.blueprint import user_api, user_blueprint
from core_app.routes.beneficiary.blueprint import beneficiary_api, beneficiary_blueprint

blueprints = [
    user_blueprint,
    health_blueprint,
    beneficiary_blueprint,
]

apis = [
    user_api,
    health_api,
    beneficiary_api,
]
