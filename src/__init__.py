from flask import Flask
from werkzeug.utils import import_string
from utils import mysql
# import utils.mysql as mysql


blueprints = [
    'src.veiws.classRoom:classRoom',
    'src.veiws.user:user',
]

dbclient = mysql.MySqldb()

# __all__ = [dbclient]
def creatapp():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)
    return app

