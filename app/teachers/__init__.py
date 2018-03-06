from flask import Blueprint

teachers = Blueprint('teachers', __name__)

from . import views