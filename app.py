from flask import Flask, request
import DatabaseManager

app = Flask(__name__)

db = DatabaseManager.firebase_hook()


@app.route('/configs', methods=['GET'])
def get_configs():
    try:
        configs = db.get_configs()
    except:
        return {'status': 404}
    return configs


@app.route('/set_score', methods=['POST'])
def set_score():
    json = request.get_json()
    user_id = json['id']
    score = json['score']

    try:
        db.save_score(user_id, score)
    except:
        return {'status': 404}

    return {'status':200 }


@app.route('/get_score/<string:uid>', methods=['GET'])
def get_score(uid):
    try:
        score = db.get_score(uid)
    except:
        return {'status': 404}

    return score


@app.route('/get_leaderboard', methods=['GET'])
def get_leaderboard():
    leaderboard = db.get_leaderboard()
    return leaderboard


if __name__ == '__main__':
    app.run()
