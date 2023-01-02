from flask import Flask, request, jsonify
from schemas import ParamsListSchema
from marshmallow import ValidationError

from utils import build_query

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run()
