from flask import Blueprint, render_template, current_app #, session

from app.models.upload import Data

upload_routes = Blueprint("upload_routes", __name__)

@upload_routes.route("/upload")
def uploads():
    upload = Upload.all()
    return render_template("upload.html", upload=upload)
