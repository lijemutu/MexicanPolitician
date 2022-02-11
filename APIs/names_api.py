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
        r = requests.get(url)
        if(r.status_code != 200):
            raise Exception(f"Request for {type} ... not valid")
        data = r.json()

        if(type == "fullName"):
            parsedData = {'forename':data['forename'],'surname':data['surname'],'secondSurname':data['secondSurname'],'countries':data['countries'][0:5]}
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
        partialNameModel = FullNameModel.PartialNameModel(name=name,typeName=type,foundCountry1=countries[0]['jurisdiction'],foundCountry1percent=float(countries[0]['incidence']),foundCountry2=countries[1]['jurisdiction'],foundCountry2percent=float(countries[1]['incidence']),foundCountry3=countries[2]['jurisdiction'],foundCountry3percent=float(countries[2]['incidence']),foundCountry4=countries[3]['jurisdiction'],foundCountry4percent=float(countries[3]['incidence']),foundCountry5=countries[4]['jurisdiction'],foundCountry5percent=float(countries[4]['incidence']))
        db.session.add(partialNameModel)
        db.session.commit()

    def saveResponseFullNameToDatabase(self,data):
        forename = data['forename']
        surname = data['surname']
        secondSurname = data['secondSurname']
        countries= data['countries']
        fullNameModel = FullNameModel(firstName=forename,lastName=surname,secondLastName=secondSurname,foundCountry1=countries[0]['jurisdiction'],foundCountry1percent=float(countries[0]['percent']),foundCountry2=countries[1]['jurisdiction'],foundCountry2percent=float(countries[1]['percent']),foundCountry3=countries[2]['jurisdiction'],foundCountry3percent=float(countries[2]['percent']),foundCountry4=countries[3]['jurisdiction'],foundCountry4percent=float(countries[3]['percent']),foundCountry5=countries[4]['jurisdiction'],foundCountry5percent=float(countries[4]['percent']))
        db.session.add(fullNameModel)
        db.session.commit()

        



