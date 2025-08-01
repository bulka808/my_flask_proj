from flask import Blueprint, render_template, request, redirect, jsonify, url_for
import os
import random
from app import db
from app.models import Comment



main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main_bp.route('/gallery', methods=["GET", "POST"])
def gallery():
    if request.method == "POST":
        name = request.form["username"]
        text = request.form["text"]

        new_comment = Comment(name=name, text=text)
        db.session.add(new_comment)
        db.session.commit()
        return redirect("/gallery")

    comments = Comment.query.all()

    img_folder = "app/static/img"
    imgs = os.listdir(img_folder)
    valid_ext = ['.jpg', '.jpeg', '.png']
    imgs = [img for img in imgs if any(img.lower().endswith(ext) for ext in valid_ext)]

    return render_template('gallery.html', imgs=imgs, comments=comments)


@main_bp.route('/api', methods=['GET'])
def api():
    img_folder = "app/static/img"
    imgs = os.listdir(img_folder)
    valid_ext = ['.jpg', '.jpeg', '.png']
    imgs = [img for img in imgs if any(img.lower().endswith(ext) for ext in valid_ext)]

    img = random.choice(imgs)
    img_url = url_for("static", filename=f"img/{img}", _external=True)

    return jsonify({"image": img, "url":img_url})


