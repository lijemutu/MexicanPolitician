import os
from flask import Flask, request
from APIs.names_api import NamesApi
from database.dbinit import db


app = Flask(__name__)
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:postgres@{POSTGRES_HOST}:5432/mex_polit_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

# TODO Refactor controllers from initialization


@app.route("/api/name", methods=["GET"])
def NameNationality():
    args = request.args

    if "fn" in args and "sn" in args:
        firstName = args["fn"]
        lastName = args.get("sn")
    else:
        return "Parameters malformed", 400

    if "ssn" in args:
        secondLastName = args["ssn"]
    else:
        secondLastName = ""

    if firstName == "" or lastName == "":
        return "You miss firstName or lastName", 400

    nameObject = NamesApi(firstName, lastName, secondLastName=secondLastName)

    nationalities = nameObject.requestFullName()
    if "error" in nationalities:
        if nationalities["error"] == 404:
            return "Elements not found", 404
        if nationalities["error"] == 500:
            return "Internal Server error with request", 500
        if nationalities["error"] == 400:
            return "Bad request", 400
    return nationalities, 200


@app.route("/api/partialname", methods=["GET"])
def PartialNameLocation():
    args = request.args

    if "name" in args and "type" in args:
        name = args["name"]
        typeName = args.get("type")
    else:
        return "Parameters malformed", 400

    if name == "" or typeName == "":
        return "You miss name or type", 400

    if not (typeName == "forename" or typeName == "surname"):
        return f"typeName '{typeName}' not valid", 400

    if typeName == "forename":
        nameObject = NamesApi(firstName=name, lastName="")
    if typeName == "surname":
        nameObject = NamesApi(firstName="", lastName=name)

    locations = nameObject.requestPartialName(typeName)
    if "error" in locations:
        if locations["error"] == 404:
            return "Elements not found", 404
        if locations["error"] == 500:
            return "Internal Server error with request", 500
        if locations["error"] == 400:
            return "Bad request", 400

    return locations, 200


if __name__ == "__main__":
    app.run()
