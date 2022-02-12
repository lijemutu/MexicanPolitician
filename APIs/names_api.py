import requests
from APIs.Api import Api
from dotenv import load_dotenv
import os
from database.tablesName import FullNameModel 
from database.tablesName import FullNameModel
from database.dbinit import db


load_dotenv()
API_KEY_NAMES = os.environ.get('API_KEY_NAMES')

class NamesApi(Api):

    def __init__(self,firstName = "",lastName = "",secondLastName = "") -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.secondLastName = secondLastName

    def requestApiServer(self,url,type):
        try:
            r = requests.get(url)
        except:
            return {'error':500}

        if(r.status_code != 200):
            raise Exception(f"Request for {type} ... not valid")
        data = r.json()

        apiErrors = ["0018"]
        if('status' in data and data['status'][0]['code'] in apiErrors):
            return {'error':400}

        if(type == "fullName"):
            if 'secondSurname' in data:
                parsedData = {'forename':data['forename'],'surname':data['surname'],'secondSurname':data['secondSurname'],'countries':data['countries'][0:5]}
            else:
                parsedData = {'forename':data['forename'],'surname':data['surname'],'countries':data['countries'][0:5]}
            self.saveResponseFullNameToDatabase(parsedData)

        else:
            parsedData = {'name':data['name'],'type':data['type'],'countries':data['jurisdictions'][0:5]}
            self.saveResponsePartialNameToDatabase(parsedData)


        return parsedData
    def requestFullName(self):

        ONO_API_FULL_NAME = f"https://ono.4b.rs/v1/nat?key={API_KEY_NAMES}&fn={self.firstName}&sn={self.lastName}&ssn={self.secondLastName}"
        return self.requestApiServer(ONO_API_FULL_NAME,"fullName")
        
    def requestPartialName(self,typeName):
        if(typeName == "forename"):
            name = self.firstName
        if(typeName == "surname"):
            name = self.lastName

        ONO_API_PARTIAL = f"https://ono.4b.rs/v1/jur?key={API_KEY_NAMES}&name={name}&type={typeName}"
        return self.requestApiServer(ONO_API_PARTIAL,typeName)
    
    
    def saveResponsePartialNameToDatabase(self,data):
        name = data['name']
        type = data['type']
        countries = data['countries']
        partialNameModel = FullNameModel.PartialNameModel(name=name,typeName=type,countries=countries)
        db.session.add(partialNameModel)
        db.session.commit()

    def saveResponseFullNameToDatabase(self,data):
        forename = data['forename']
        surname = data['surname']
        if 'secondSurname' in data:
            secondSurname = data['secondSurname']
        else:
            secondSurname = ""
        countries= data['countries']
        fullNameModel = FullNameModel(firstName=forename,lastName=surname,secondLastName=secondSurname,countries=countries)
        db.session.add(fullNameModel)
        db.session.commit()

        



