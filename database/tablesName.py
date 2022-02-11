import datetime
from database.dbinit import db

class FullNameModel(db.Model):
    __tablename__ = 'fullnamestb'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128), nullable=False)
    lastName = db.Column(db.String(128), nullable=False)
    secondLastName = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime)
    foundCountry1 = db.Column(db.String(128),nullable=False)
    foundCountry1percent = db.Column(db.Float,nullable=False)
    foundCountry2 = db.Column(db.String(128),nullable=True)
    foundCountry2percent = db.Column(db.Float,nullable=True)
    foundCountry3 = db.Column(db.String(128),nullable=True)
    foundCountry3percent = db.Column(db.Float,nullable=True)
    foundCountry4 = db.Column(db.String(128),nullable=True)
    foundCountry4percent = db.Column(db.Float,nullable=True)
    foundCountry5 = db.Column(db.String(128),nullable=True)
    foundCountry5percent = db.Column(db.Float,nullable=True)

    def __init__(self
                ,firstName
                ,lastName
                ,secondLastName
                ,foundCountry1
                ,foundCountry1percent
                ,foundCountry2
                ,foundCountry2percent
                ,foundCountry3
                ,foundCountry3percent
                ,foundCountry4
                ,foundCountry4percent
                ,foundCountry5
                ,foundCountry5percent):
        self.firstName = firstName
        self.lastName = lastName
        self.secondLastName = secondLastName
        self.created_at = datetime.datetime.utcnow()
        self.foundCountry1 = foundCountry1
        self.foundCountry1percent = foundCountry1percent
        self.foundCountry2 = foundCountry2
        self.foundCountry2percent = foundCountry2percent
        self.foundCountry3 = foundCountry3
        self.foundCountry3percent = foundCountry3percent
        self.foundCountry4 = foundCountry4
        self.foundCountry4percent = foundCountry4percent
        self.foundCountry5 = foundCountry5
        self.foundCountry5percent = foundCountry5percent

    class PartialNameModel(db.Model):
        __tablename__ = "partialnamestb"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128), nullable=False)
        typeName = db.Column(db.String(128), nullable=False)
        created_at = db.Column(db.DateTime)
        foundCountry1 = db.Column(db.String(128),nullable=False)
        foundCountry1percent = db.Column(db.Float,nullable=False)
        foundCountry2 = db.Column(db.String(128),nullable=True)
        foundCountry2percent = db.Column(db.Float,nullable=True)
        foundCountry3 = db.Column(db.String(128),nullable=True)
        foundCountry3percent = db.Column(db.Float,nullable=True)
        foundCountry4 = db.Column(db.String(128),nullable=True)
        foundCountry4percent = db.Column(db.Float,nullable=True)
        foundCountry5 = db.Column(db.String(128),nullable=True)
        foundCountry5percent = db.Column(db.Float,nullable=True)
        
        def __init__(self
                ,name
                ,typeName
                ,foundCountry1
                ,foundCountry1percent
                ,foundCountry2
                ,foundCountry2percent
                ,foundCountry3
                ,foundCountry3percent
                ,foundCountry4
                ,foundCountry4percent
                ,foundCountry5
                ,foundCountry5percent):
            self.name = name
            self.typeName = typeName
            self.created_at = datetime.datetime.utcnow()
            self.foundCountry1 = foundCountry1
            self.foundCountry1percent = foundCountry1percent
            self.foundCountry2 = foundCountry2
            self.foundCountry2percent = foundCountry2percent
            self.foundCountry3 = foundCountry3
            self.foundCountry3percent = foundCountry3percent
            self.foundCountry4 = foundCountry4
            self.foundCountry4percent = foundCountry4percent
            self.foundCountry5 = foundCountry5
            self.foundCountry5percent = foundCountry5percent

