import requests

class NamesApi:


    def __init__(self,firstName,lastName) -> None:
        self.firstName = firstName
        self.lastName = lastName

    def requestNationality(self):
        ONO_API = "https://ono.4b.rs/v1/nat"
        r = requests.get(ONO_API)
        if(r.status_code != 200):
            raise Exception(f"Request for name ... not valid")

