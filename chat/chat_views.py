# add views (endpoints) in chat/chat_views.py
from flask import Blueprint

chat_app = Blueprint('chat', __name__)


@chat_app.route('/chat')
def chat():
    return 'chat'
