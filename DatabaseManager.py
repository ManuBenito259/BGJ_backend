import secrets
import pyrebase


class firebase_hook:
    def __init__(self):
        self.configs = secrets.FIREBASE_CONFIG
        self.firebase = pyrebase.initialize_app(self.configs)
        self.db = self.firebase.database()
        self.auth = self.firebase.auth()


    def get_configs(self):
        configs = self.db.child("configs").get()
        return configs

    def save_score(self, id, score):
        data = {'score': score}
        self.db.child("users").child(id).set(data)

    def get_score(self, id):
        return self.db.child("users").child(id).child("score").get().val()

    def get_leaderboard(self):
        users = self.db.child("users").get()
        leaderboard = {}

        for u in users.each():
            id = u.key()
            score = u.val()['score']
            leaderboard[id] = score

        return leaderboard #{k: v for k, v in sorted(leaderboard.items(), key=lambda item: item[1])}

