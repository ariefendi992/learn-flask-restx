from flask import Flask, jsonify
from core.models.models import Course
from settings import Config
from core.resource import resoure_namespace
from core.dependencies import api, db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api.init_app(app)
    db.init_app(app)

    resoure_namespace(api)

    return app


app = create_app()


@app.route("/data")
def index():
    sql = Course.query.all()

    data = []
    for i in sql:
        data.append({"id": i.id, "name": i.name})

    return jsonify(data=data)
