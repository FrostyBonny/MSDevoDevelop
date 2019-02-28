from flask import Blueprint

classRoom = Blueprint('classRoom', __name__, url_prefix='/classRoom')

from . import veiw