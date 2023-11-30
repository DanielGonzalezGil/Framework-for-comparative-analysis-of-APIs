from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database connection for PostgreSQL
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://postgres:b9willoltoby@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Dont need but added to stop console from giving warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize DB
db = SQLAlchemy(app)

# initialize ma
ma = Marshmallow(app)


# Product Class/Model
class NBAPlayer(db.Model):
    __tablename__ = "nba_players"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    team = db.Column(db.String(100))
    position = db.Column(db.String(50))
    height = db.Column(db.String(10))
    weight = db.Column(db.Numeric(5, 2))
    points_per_game = db.Column(db.Numeric(5, 2))
    assists_per_game = db.Column(db.Numeric(5, 2))
    rebounds_per_game = db.Column(db.Numeric(5, 2))


# NBAPlayer Schema
class NBAPlayerSchema(ma.Schema):
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


# Initialize schema
nba_player_schema = NBAPlayerSchema()
nba_players_schema = NBAPlayerSchema(many=True)


# Create an NBAPlayer
@app.route("/nba_player", methods=["POST"])
def add_nba_player():
    name = request.json["name"]
    team = request.json["team"]
    position = request.json["position"]
    height = request.json["height"]
    weight = request.json["weight"]
    points_per_game = request.json["points_per_game"]
    assists_per_game = request.json["assists_per_game"]
    rebounds_per_game = request.json["rebounds_per_game"]

    new_nba_player = NBAPlayer(
        name=name,
        team=team,
        position=position,
        height=height,
        weight=weight,
        points_per_game=points_per_game,
        assists_per_game=assists_per_game,
        rebounds_per_game=rebounds_per_game,
    )

    db.session.add(new_nba_player)
    db.session.commit()

    return nba_player_schema.jsonify(new_nba_player)


# API route to serve the HTML template
@app.route("/")
def index():
    return render_template("index.html")


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
