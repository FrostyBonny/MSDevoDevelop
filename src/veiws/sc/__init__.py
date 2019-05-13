from flask import Blueprint

sc = Blueprint('sc', __name__, url_prefix='/sc')

from . import veiw