from flask import Flask, request

from APIs.names_api import NamesApi

app = Flask(__name__)

from db.tablesName import db

db.init_app(app)

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
    #TODO paging and formatting results
    
    return nationalities,200

@app.route("/api/partialname",methods = ["GET"])
def PartialNameLocation():
    args = request.args

    if "name" in args:
        name = args["name"]

    if "type" in args:
        typeName = args.get("type")

    if name == "" or typeName == "":
        return "You miss name or type",400
    
    if(typeName == "forename"):
        nameObject = NamesApi(firstName= name,lastName="")
    if(typeName == "surname"):
        nameObject = NamesApi(firstName="",lastName=name)

    locations = nameObject.requestPartialName(typeName)
    
    #TODO paging and formatting results
    return locations,200