from flask import Flask, request

from APIs.names_api import NamesApi

app = Flask(__name__)

@app.route("/api/name",methods = ["GET"])
def NameNationality():
    args = request.args

    if "fn" in args:
        firstName = args["fn"]

    if "sn" in args:
        lastName = args.get("sn")

    if "ssn" in args:
        secondLastName = args["ssn"]
    if firstName == "" or lastName == "":
        return "You miss firstName or lastName",400
    nameObject = NamesApi(firstName,lastName,secondLastName=secondLastName)
    nationalities = nameObject.requestFullName()
    
    return nationalities,200