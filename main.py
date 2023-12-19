from flask import Flask, request, jsonify
from flask_json import FlaskJSON
from model.Twit import Twit


app = Flask(__name__)
json = FlaskJSON()
twits = []
n = 0


@json.encoder
def custom_encoder(obj):
    if isinstance(obj, Twit):
        return {'twit_id': obj.twit_id, 'body': obj.body, 'author': obj.author}


json.init_app(app)


@app.route('/twits', methods=['POST'])
def create_twit():
    global n
    twit_json = request.get_json()
    twit = Twit(n, twit_json['body'], twit_json['author'])
    twits.append(twit)
    n = n + 1
    return jsonify({'status': 'successfully created'})


@app.route('/twits', methods=['GET'])
def read_twits():
    return jsonify({'twits': twits})


@app.route('/twits/<twit_num>', methods=['GET'])
def read_twit(twit_num):
    try:
        return jsonify({'twit': twits[int(twit_num)]})
    except IndexError:
        return "This twit does not exist"


@app.route('/twits/<twit_num>', methods=['DELETE'])
def del_twit(twit_num):
    try:
        twits[int(twit_num)].del_twit()
        return jsonify({'status': 'successfully deleted'})
    except IndexError:
        return "This twit does not exist"


@app.route('/twits/<twit_num>', methods=['PUT'])
def change_twit(twit_num):
    twit_json = request.get_json()
    try:
        twits[int(twit_num)].change_twit(twit_json['body'])
        return jsonify({'status': 'successfully changed'})
    except IndexError:
        return "This twit does not exist"



if __name__ == '__main__':
    app.run(debug=True)
