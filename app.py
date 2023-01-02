import os

from flask import Flask, request, jsonify

from db import db
from schemas import ParamsListSchema
from marshmallow import ValidationError

from utils import build_query

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат


    try:
        params = ParamsListSchema().load(request.json)
    except ValidationError as ex:
        return ex.messages, '400'

    result = None

    for query in params["queries"]:
        result = build_query(cmd=query["cmd"], param=query["value"], data=result)

    return jsonify(result), 200


@app.route("/test_db")
def test_db():
    result = db.session.execute("""
        SELECT 1
    """).scalar()

    return jsonify({
        'result': result
    })


if __name__ == "__main__":
    app.run()
