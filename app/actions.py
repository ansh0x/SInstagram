from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from . import app, db

from .models import *

action = Blueprint('action', __name__)

@action.route('/like-post', methods=['POST', 'GET'])
def like():
    
    print("req posted")
    postId = request.get_json().get('postId')

    post = Posts.query.filter_by(id=postId).first()

    if current_user in post.likes:
        print('already liked')
        post.likes.remove(current_user)
    else:
        post.likes.append(current_user)

    db.session.commit()

    total_likes = post.total_likes()
    print(total_likes)
    print(type(total_likes))

    return jsonify({'total_likes' : total_likes})

