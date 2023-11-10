from server import app, db
from server.models import User, PublicCharger, PrivateCharger, Message, Review
from flask import Flask
import datetime as dt

def populate_users():
    # Insert User records
    user1 = User(username="Otto", email="otto.kth@mail.com", ThumbsUp=0, ThumbsDown=300)
    user2 = User(username="Oscar", email="Oscar-EVKing@ShargeApp.se", ThumbsUp=1, ThumbsDown=29)
    user3 = User(username="Adrian", email="Adrian@mail.se", ThumbsUp=4, ThumbsDown=5)
    user4 = User(username="Jacob", email="Jacob@InterviewHero.com", ThumbsUp=5000000, ThumbsDown=0)
    user5 = User(username="Tina", email="Tina@FigmaGod.com", ThumbsUp=10, ThumbsDown=5)
    
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.commit()

def populate_public_chargers():
    # Insert PublicCharger records
    charger1 = PublicCharger(
        OwnedBy="Vattenfall SE",
        PowerKw=150,
        NumberChargingPoints=4,
        Connector="2 = CSS",
        Open24h=True,
        Lat=59.34733878,
        Lng=18.2340858,
        RealTimeInformation=True,
        ConnectorID=94835432,
        ConnectorNumber=1,
        ConnectorSensorStatus="1 = Available",
        Price=6.99
    )
    charger2 = PublicCharger(
        OwnedBy="EON",
        PowerKw=50,
        NumberChargingPoints=3,
        Connector="1 = Type 2",
        Open24h=False,
        Lat=58.34733878,
        Lng=17.8340858,
        RealTimeInformation=False,
        ConnectorID=13054981,
        ConnectorNumber=4,
        ConnectorSensorStatus="0 = Unavailable",
        Price=4.654
    )
    
    db.session.add(charger1)
    db.session.add(charger2)
    db.session.commit()

def populate_private_chargers():
    # Insert PrivateCharger records
    charger1 = PrivateCharger(
        OwnerID=135246,
        PowerKw=11,
        Brand="Zaptec",
        Model="Go",
        Connector="1 = Type2",
        ChargepointName="Ottos Chargepoint #1",
        Lat=62.05324,
        Lng=79.52859,
        InfoboxAvailability="Usually this will be available on Tuesdays & Thursdays between 9-18...",
        InfoboxUserInstructions="Step 1: Go outside the garage outside house 23\nStep 2: Locate the Yale Doorsman lock\nStep 3: Use the pincode 5355 to open the ...\nStep 4: Send me a message and I will start the charge.",
        PriceKrPerKwh=2.33,
        ImageID=3425987
    )
    charger2 = PrivateCharger(
        OwnerID=642135,
        PowerKw=22,
        Brand="Garo",
        Model="Entity Pro",
        Connector="2 = CSS",
        ChargepointName="Jacobs Mek o Smek UF",
        Lat=58.9543987,
        Lng=17.439,
        InfoboxAvailability="Weekdays 7-16",
        InfoboxUserInstructions="Message me",
        PriceKrPerKwh=3.49,
        ImageID=9321847
    )
    charger3 = PrivateCharger(
        OwnerID=456123,
        PowerKw=22,
        Brand="Charge Amps",
        Model="Aura",
        Connector="3 = Chmod",
        ChargepointName="Adrians ladd AB",
        Lat=59.34733878,
        Lng=18.2340858,
        InfoboxAvailability="ONLY SUNDAYS all day",
        InfoboxUserInstructions="Plugg and play",
        PriceKrPerKwh=3.87,
        ImageID=9123847
    )
    
    db.session.add(charger1)
    db.session.add(charger2)
    db.session.add(charger3)
    db.session.commit()

def populate_messages():
    # Insert Message records
    message1 = Message(
        SentByUserID=135246,
        SentToUserID=642135,
        MessageNumber=1,
        SentAt=dt.datetime(2019,1,2,12,6,2),
        Content="Hey Can I book your charger tomorrow, 8-14",
        RequestStatus="0 = Declined"
    )
    message2 = Message(
        SentByUserID=642135,
        SentToUserID=456123,
        MessageNumber=23,
        SentAt=dt.datetime(2023,11,2,18,34,32),
        Content="Why did you not tell me the price before???",
        RequestStatus="1 = Pending"
    )
    message3 = Message(
        SentByUserID=456123,
        SentToUserID=642135,
        MessageNumber=2,
        SentAt=dt.datetime(2084,9,10,4,50,52),
        Content="Thanks see you at 5 pm tomorrow!",
        RequestStatus="2 = Accepted"
    )
    
    db.session.add(message1)
    db.session.add(message2)
    db.session.add(message3)
    db.session.commit()

def populate_reviews():
    # Insert Review records
    review1 = Review(
        SentFromID=9283457,
        SentToID=135246,
        IsPositive=True,
        Comment="Hey Can I book your charger tomorrow, 8-14",
        Date=dt.datetime(2023,5,8,22,15,00)
    )
    review2 = Review(
        SentFromID=3429435,
        SentToID=642135,
        IsPositive=False,
        Comment="Why did you not tell me the price before???",
        Date=dt.datetime(2023,7,21,19,31,00)
    )
    review3 = Review(
        SentFromID=4302599,
        SentToID=456123,
        IsPositive=True,
        Comment="Thanks see you at 5 pm tomorrow!",
        Date=dt.datetime(2023,8,10,17,50,52)
    )

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.commit()


def create_app():
    # Create a Flask app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Update with your database URL

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Create the database
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    
    # Populate the users
    with app.app_context():
        populate_users()
        populate_public_chargers()
        populate_private_chargers()
        populate_messages()
        populate_reviews()