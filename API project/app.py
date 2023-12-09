from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
from sqlalchemy import URL

# initialize app
app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

# connection to database
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://postgres:password@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Dont need but added to stop console from giving warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize DB
db = SQLAlchemy(app)

# initialize ma
ma = Marshmallow(app)


class NBAplayerStatsTable(db.Model):
    __tablename__ = "nba_players"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    team = db.Column(db.String(100))
    position = db.Column(db.String(50))
    height = db.Column(db.String(10))
    weight = db.Column(db.Float(5, 2))
    points_per_game = db.Column(db.Float(5, 2))
    assists_per_game = db.Column(db.Float(5, 2))
    rebounds_per_game = db.Column(db.Float(5, 2))

    def __init__(
        self,
        name,
        team,
        position,
        height,
        weight,
        points_per_game,
        assists_per_game,
        rebounds_per_game,
    ):
        self.name = name
        self.team = team
        self.position = position
        self.height = height
        self.weight = weight
        self.points_per_game = points_per_game
        self.assists_per_game = assists_per_game
        self.rebounds_per_game = rebounds_per_game


# Schema
class NBAtestSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "team",
            "position",
            "height",
            "weight",
            "points_per_game",
            "assists_per_game",
            "rebounds_per_game",
        )


nba_test_schema = NBAtestSchema()
nba_tests_schema = NBAtestSchema(many=True)


# GET endpoint
@app.route("/Get_nba_players", methods=["GET"])
def get_nba_player():
    all_players = NBAplayerStatsTable.query.all()
    result = nba_tests_schema.dump(all_players)
    return jsonify(result)


# POST endpoint
@app.route("/Post_nba_players", methods=["POST"])
def add_player():
    name = request.json["name"]
    team = request.json["team"]
    position = request.json["position"]
    height = request.json["height"]
    weight = request.json["weight"]
    points_per_game = request.json["points_per_game"]
    assists_per_game = request.json["assists_per_game"]
    rebounds_per_game = request.json["rebounds_per_game"]

    record = NBAplayerStatsTable(
        name,
        team,
        position,
        height,
        weight,
        points_per_game,
        assists_per_game,
        rebounds_per_game,
    )
    db.session.add(record)
    db.session.commit()
    return nba_test_schema.jsonify(record)


# PATCH endpoint
@app.route("/Update_nba_player/<int:id>", methods=["PATCH"])
def update_player(id):
    player = NBAplayerStatsTable.query.get(id)

    if not player:
        return jsonify({"message": "Player not found"}), 404

    data = request.json
    player.name = data.get("name", player.name)
    player.team = data.get("team", player.team)
    player.position = data.get("position", player.position)
    player.height = data.get("height", player.height)
    player.weight = data.get("weight", player.weight)
    player.points_per_game = data.get("points_per_game", player.points_per_game)
    player.assists_per_game = data.get("assists_per_game", player.assists_per_game)
    player.rebounds_per_game = data.get("rebounds_per_game", player.rebounds_per_game)

    db.session.commit()
    return nba_test_schema.jsonify(player)


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
