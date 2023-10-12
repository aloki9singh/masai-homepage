from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "port"
app.config["MYSQL_DB"] = "flask_app"
mysql = MySQL(app)

from app.controllers import user_controller

if __name__ == "__main__":
    app.run(debug=True)
