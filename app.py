from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from models.user import User
from routes.auth import auth as auth_blueprint
from routes.payment import payment as payment_blueprint
from errors.handlers import errors as error_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(payment_blueprint)
app.register_blueprint(error_blueprint)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == "__main__":
    app.run(debug=True)
