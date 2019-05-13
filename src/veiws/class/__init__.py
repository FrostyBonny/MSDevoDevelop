from flask import Blueprint

my_class = Blueprint('my_class', __name__, url_prefix='/class')

from . import veiw