from flask import Flask
from database import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

#SQLALCHEMY_DATABASE_URI = 'postgres://username:password@localhost/dbname'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db.init_app(app)

from routes.user import user_blueprint
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        db.create_all()  
    app.run(debug=True)
    