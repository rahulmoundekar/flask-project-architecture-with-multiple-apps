from flask import Blueprint

feed_app = Blueprint('feed', __name__)


@feed_app.route('/feed')
def feed():
    return 'feed'
