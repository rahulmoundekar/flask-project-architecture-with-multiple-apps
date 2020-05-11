# register blueprint and start flask app
from flask import Flask

from feed import feed_views, fee_news_views
from chat import chat_views

app = Flask(__name__, instance_relative_config=False)
app.register_blueprint(feed_views.feed_app)
app.register_blueprint(fee_news_views.feed_news_app)
app.register_blueprint(chat_views.chat_app)

app.run(debug=True)
