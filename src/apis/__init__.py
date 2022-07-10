from flask import Blueprint

from src.apis.articles import bp_api_articles
from src.apis.tags import bp_api_tags


bp_api = Blueprint('apis', __name__, url_prefix='/api')
bp_api.register_blueprint(bp_api_articles)
bp_api.register_blueprint(bp_api_tags)
