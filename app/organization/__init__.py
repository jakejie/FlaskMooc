from flask import Blueprint

organization = Blueprint('organization', __name__)

from . import views