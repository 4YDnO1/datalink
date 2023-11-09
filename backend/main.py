from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from utils import get_pages, generate_answer

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False


@app.post('/get_questions')
@cross_origin()
def generate_questions():
    json: dict = request.json
    question = json.get("question")

    if not question:
        return jsonify({"message": "DRUAK"})

    response = Response(get_pages(app, question))
    response.headers['Content-Type'] = 'application/json'

    return response


@app.post('/answer_question')
@cross_origin()
def answer_question():
    json: dict = request.json
    answer = generate_answer(json)

    return jsonify(answer)


if __name__ == '__main__':
    app.run(debug=True)
