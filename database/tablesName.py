import datetime
from database.dbinit import db


class FullNameModel(db.Model):
    __tablename__ = "fullnamestb"

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128), nullable=False)
    lastName = db.Column(db.String(128), nullable=False)
    secondLastName = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime)
    foundCountry1 = db.Column(db.String(128), nullable=False)
    foundCountry1percent = db.Column(db.Float, nullable=False)
    foundCountry2 = db.Column(db.String(128), nullable=True)
    foundCountry2percent = db.Column(db.Float, nullable=True)
    foundCountry3 = db.Column(db.String(128), nullable=True)
    foundCountry3percent = db.Column(db.Float, nullable=True)
    foundCountry4 = db.Column(db.String(128), nullable=True)
    foundCountry4percent = db.Column(db.Float, nullable=True)
    foundCountry5 = db.Column(db.String(128), nullable=True)
    foundCountry5percent = db.Column(db.Float, nullable=True)

    def __init__(self, firstName, lastName, secondLastName, countries: list):
        self.firstName = firstName
        self.lastName = lastName
        self.secondLastName = secondLastName
        self.created_at = datetime.datetime.utcnow()

        try:
            self.foundCountry1 = countries[0]["jurisdiction"]
        except IndexError:
            self.foundCountry1 = ""
        try:
            self.foundCountry1percent = float(countries[0]["percent"])
        except IndexError:
            self.foundCountry1percent = 0

        try:
            self.foundCountry2 = countries[1]["jurisdiction"]
        except IndexError:
            self.foundCountry2 = ""
        try:
            self.foundCountry2percent = float(countries[1]["percent"])
        except IndexError:
            self.foundCountry2percent = 0

        try:
            self.foundCountry3 = countries[2]["jurisdiction"]
        except IndexError:
            self.foundCountry3 = ""
        try:
            self.foundCountry3percent = float(countries[2]["percent"])
        except IndexError:
            self.foundCountry3percent = 0

        try:
            self.foundCountry4 = countries[3]["jurisdiction"]
        except IndexError:
            self.foundCountry4 = ""
        try:
            self.foundCountry4percent = float(countries[3]["percent"])
        except IndexError:
            self.foundCountry4percent = 0

        try:
            self.foundCountry5 = countries[4]["jurisdiction"]
        except IndexError:
            self.foundCountry5 = ""
        try:
            self.foundCountry5percent = float(countries[4]["percent"])
        except IndexError:
            self.foundCountry5percent = 0

    class PartialNameModel(db.Model):
        __tablename__ = "partialnamestb"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128), nullable=False)
        typeName = db.Column(db.String(128), nullable=False)
        created_at = db.Column(db.DateTime)
        foundCountry1 = db.Column(db.String(128), nullable=False)
        foundCountry1percent = db.Column(db.Float, nullable=False)
        foundCountry2 = db.Column(db.String(128), nullable=True)
        foundCountry2percent = db.Column(db.Float, nullable=True)
        foundCountry3 = db.Column(db.String(128), nullable=True)
        foundCountry3percent = db.Column(db.Float, nullable=True)
        foundCountry4 = db.Column(db.String(128), nullable=True)
        foundCountry4percent = db.Column(db.Float, nullable=True)
        foundCountry5 = db.Column(db.String(128), nullable=True)
        foundCountry5percent = db.Column(db.Float, nullable=True)

        def __init__(self, name, typeName, countries: list):
            self.name = name
            self.typeName = typeName
            self.created_at = datetime.datetime.utcnow()

            try:
                self.foundCountry1 = countries[0]["jurisdiction"]
            except IndexError:
                self.foundCountry1 = ""
            try:
                self.foundCountry1percent = float(countries[0]["incidence"])
            except IndexError:
                self.foundCountry1percent = 0

            try:
                self.foundCountry2 = countries[1]["jurisdiction"]
            except IndexError:
                self.foundCountry2 = ""
            try:
                self.foundCountry2percent = float(countries[1]["incidence"])
            except IndexError:
                self.foundCountry2percent = 0

            try:
                self.foundCountry3 = countries[2]["jurisdiction"]
            except IndexError:
                self.foundCountry3 = ""
            try:
                self.foundCountry3percent = float(countries[2]["incidence"])
            except IndexError:
                self.foundCountry3percent = 0

            try:
                self.foundCountry4 = countries[3]["jurisdiction"]
            except IndexError:
                self.foundCountry4 = ""
            try:
                self.foundCountry4percent = float(countries[3]["incidence"])
            except IndexError:
                self.foundCountry4percent = 0

            try:
                self.foundCountry5 = countries[4]["jurisdiction"]
            except IndexError:
                self.foundCountry5 = ""
            try:
                self.foundCountry5percent = float(countries[4]["incidence"])
            except IndexError:
                self.foundCountry5percent = 0
