from flask import Flask, jsonify, request
from functions import resolve_list_consistently
app = Flask(__name__)


@app.route('/api/resolve', methods=['GET'])
def resolver():
    data = request.json
    try:
        funcs = data['rule']
        values = data['data']
        result = resolve_list_consistently(funcs, values)
    except (TypeError, KeyError):
        return jsonify({'message': 'Bad Request'})
    else:
        return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
