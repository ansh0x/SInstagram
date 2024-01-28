from flask import Blueprint, request, jsonify
from flask_login import current_user
from app import db

from app.models import *

action = Blueprint('action', __name__)

@action.route('/like-post', methods=['POST', 'GET'])
def like():
    
    postId = request.get_json().get('postId')

    post = Posts.query.filter_by(id=postId).first()

    if current_user in post.likes:
        post.likes.remove(current_user)
    else:
        post.likes.append(current_user)

    db.session.commit()

    total_likes = post.total_likes()

    return jsonify({'total_likes' : total_likes})

@action.route('/delete-post', methods=['Post'])
def delete_post():

    postId = request.get_json().get('postId')

    post = Posts.query.filter_by(id=postId).first()

    db.session.delete(post)
    db.session.commit()

    posts = Posts.query.filter_by(user_id=current_user.id).all()

    return jsonify({'posts' : posts})


