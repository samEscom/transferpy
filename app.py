from flask_jwt_extended import JWTManager

from core_app.setup import create_app

app = create_app(__name__)

app.config["JWT_SECRET_KEY"] = "password_super_secreta_ja_ja_ja"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 1800 * 3  # 1800 seconds = 30 minutes
jwt = JWTManager(app)

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    app.run(debug=True, host="0.0.0.0", port=8000)
