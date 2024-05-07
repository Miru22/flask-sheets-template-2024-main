from flask import Blueprint, render_template #, current_app #, session

upload_routes = Blueprint("upload_routes", __name__)

@upload_routes.route("/")
@upload_routes.route("/upload")
def index():
    return render_template("upload.html")

@upload_routes.route("/about")
def about():
    return render_template("about.html")