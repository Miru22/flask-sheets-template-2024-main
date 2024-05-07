from flask import Blueprint, render_template, current_app #, session

from app.models.data import Data

data_routes = Blueprint("data_routes", __name__)

@data_routes.route("/data")
def datas():
    data = Data.all()
    return render_template("data.html", data=data)
