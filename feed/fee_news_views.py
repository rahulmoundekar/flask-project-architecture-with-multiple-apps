from flask import Blueprint

feed_news_app = Blueprint('news', __name__)


@feed_news_app.route('/news')
def feed():
    return 'news'
