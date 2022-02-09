from flask import request
import requests
from APIs.Api import Api
from dotenv import load_dotenv
import os 

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
        return data        
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


