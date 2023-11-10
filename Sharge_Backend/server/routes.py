from server import app,db
from server.models import User, PublicCharger, PrivateCharger, Message, Review
from flask import request, jsonify, Blueprint
from sqlalchemy.exc import IntegrityError

routes_blueprint = Blueprint('routes', __name__)

# Create a user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(**data)

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Username and email already exist for another user. Please try something else."}), 400


    
    return jsonify({"message": "User created successfully"}), 201

# Read all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    user_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(user_list)

# Read a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"id": user.id, "username": user.username, "email": user.email})
    return jsonify({"message": "User not found"}), 404

# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    for key, value in data.items():
        setattr(user, key, value)

    db.session.commit()
    return jsonify({"message": "User updated successfully"})

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})

# Create a public charger
@app.route('/public-chargers', methods=['POST'])
def create_public_charger():
    data = request.json
    charger = PublicCharger(**data)
    db.session.add(charger)
    db.session.commit()
    return jsonify({"message": "Public charger created successfully"}), 201

# Read all public chargers
@app.route('/public-chargers', methods=['GET'])
def get_all_public_chargers():
    chargers = PublicCharger.query.all()
    charger_list = [{"ChargespotID": charger.ChargespotID, "OwnedBy": charger.OwnedBy, "PowerKw": charger.PowerKw, "Price": charger.Price} for charger in chargers]
    return jsonify(charger_list)

# Read a specific public charger
@app.route('/public-chargers/<int:charger_id>', methods=['GET'])
def get_public_charger(charger_id):
    charger = PublicCharger.query.get(charger_id)
    if charger:
        return jsonify({"ChargespotID": charger.ChargespotID, "OwnedBy": charger.OwnedBy, "PowerKw": charger.PowerKw, "Price": charger.Price})
    return jsonify({"message": "Public charger not found"}), 404

# Update a public charger
@app.route('/public-chargers/<int:charger_id>', methods=['PUT'])
def update_public_charger(charger_id):
    charger = PublicCharger.query.get(charger_id)
    if not charger:
        return jsonify({"message": "Public charger not found"}), 404

    data = request.json
    for key, value in data.items():
        setattr(charger, key, value)

    db.session.commit()
    return jsonify({"message": "Public charger updated successfully"})

# Delete a public charger
@app.route('/public-chargers/<int:charger_id>', methods=['DELETE'])
def delete_public_charger(charger_id):
    charger = PublicCharger.query.get(charger_id)
    if not charger:
        return jsonify({"message": "Public charger not found"}), 404

    db.session.delete(charger)
    db.session.commit()
    return jsonify({"message": "Public charger deleted successfully"})

# Create a private charger
@app.route('/private-chargers', methods=['POST'])
def create_private_charger():
    data = request.json
    charger = PrivateCharger(**data)
    db.session.add(charger)
    db.session.commit()
    return jsonify({"message": "Private charger created successfully"}), 201

# Read all private chargers
@app.route('/private-chargers', methods=['GET'])
def get_all_private_chargers():
    chargers = PrivateCharger.query.all()
    charger_list = [{"ChargespotID": charger.ChargespotID, "OwnerID": charger.OwnerID, "PowerKw": charger.PowerKw, "PriceKrPerKwh": charger.PriceKrPerKwh} for charger in chargers]
    return jsonify(charger_list)

# Read a specific private charger
@app.route('/private-chargers/<int:charger_id>', methods=['GET'])
def get_private_charger(charger_id):
    charger = PrivateCharger.query.get(charger_id)
    if charger:
        return jsonify({"ChargespotID": charger.ChargespotID, "OwnerID": charger.OwnerID, "PowerKw": charger.PowerKw, "PriceKrPerKwh": charger.PriceKrPerKwh})
    return jsonify({"message": "Private charger not found"}), 404

# Update a private charger
@app.route('/private-chargers/<int:charger_id>', methods=['PUT'])
def update_private_charger(charger_id):
    charger = PrivateCharger.query.get(charger_id)
    if not charger:
        return jsonify({"message": "Private charger not found"}), 404

    data = request.json
    for key, value in data.items():
        setattr(charger, key, value)

    db.session.commit()
    return jsonify({"message": "Private charger updated successfully"})

# Delete a private charger
@app.route('/private-chargers/<int:charger_id>', methods=['DELETE'])
def delete_private_charger(charger_id):
    charger = PrivateCharger.query.get(charger_id)
    if not charger:
        return jsonify({"message": "Private charger not found"}), 404

    db.session.delete(charger)
    db.session.commit()
    return jsonify({"message": "Private charger deleted successfully"})
