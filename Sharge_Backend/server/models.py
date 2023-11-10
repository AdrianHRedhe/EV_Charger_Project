from server import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    ThumbsUp = db.Column(db.Integer)
    ThumbsDown = db.Column(db.Integer)
    __table_args__ = {'extend_existing': True}


class PublicCharger(db.Model):
    ChargespotID = db.Column(db.Integer, primary_key=True)
    OwnedBy = db.Column(db.String(255))
    PowerKw = db.Column(db.Integer)
    NumberChargingPoints = db.Column(db.Integer)
    Connector = db.Column(db.String(255))
    Open24h = db.Column(db.Boolean)
    Lat = db.Column(db.Float)
    Lng = db.Column(db.Float)
    RealTimeInformation = db.Column(db.Boolean)
    ConnectorID = db.Column(db.Integer)
    ConnectorNumber = db.Column(db.Integer)
    ConnectorSensorStatus = db.Column(db.Integer)
    Price = db.Column(db.Float)
    __table_args__ = {'extend_existing': True}


class PrivateCharger(db.Model):
    ChargespotID = db.Column(db.Integer, primary_key=True)
    OwnerID = db.Column(db.Integer)
    PowerKw = db.Column(db.Integer)
    Brand = db.Column(db.String(255))
    Model = db.Column(db.String(255))
    Connector = db.Column(db.Integer)
    ChargepointName = db.Column(db.String(255))
    Lat = db.Column(db.Float)
    Lng = db.Column(db.Float)
    InfoboxAvailability = db.Column(db.String(255))
    InfoboxUserInstructions = db.Column(db.String(255))
    PriceKrPerKwh = db.Column(db.Float)
    ImageID = db.Column(db.Integer)
    __table_args__ = {'extend_existing': True}


class Message(db.Model):
    MessageID = db.Column(db.Integer, primary_key=True)
    SentByUserID = db.Column(db.Integer)
    SentToUserID = db.Column(db.Integer)
    MessageNumber = db.Column(db.Integer)
    SentAt = db.Column(db.DateTime)
    Content = db.Column(db.String)
    RequestStatus = db.Column(db.Integer)
    __table_args__ = {'extend_existing': True}


class Review(db.Model):
    ReviewID = db.Column(db.Integer, primary_key=True)
    SentFromID = db.Column(db.Integer)
    SentToID = db.Column(db.Integer)
    IsPositive = db.Column(db.Boolean)
    Comment = db.Column(db.String)
    Date = db.Column(db.DateTime)
    __table_args__ = {'extend_existing': True}
