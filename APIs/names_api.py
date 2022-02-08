import requests
from APIs.Api import Api
from dotenv import load_dotenv
import os 

load_dotenv()
API_KEY_NAMES = os.environ.get('API_KEY_NAMES')

class NamesApi(Api):

    def __init__(self,firstName,lastName,secondLastName = "") -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.secondLastName = secondLastName
        


    def request(self):
        ONO_API = f"https://ono.4b.rs/v1/nat?key={API_KEY_NAMES}&fn={self.firstName}&sn={self.lastName}&ssn={self.secondLastName}"
        r = requests.get(ONO_API)
        if(r.status_code != 200):
            raise Exception(f"Request for name ... not valid")
        nationalityData = r.json()
        return nationalityData

