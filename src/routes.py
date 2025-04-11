from flask import Blueprint, jsonify, request
from models import db, User, Character, Planet, Vehicle, Favorite

api = Blueprint('api', __name__)


# Rutas personajes # 

@api.route('/people', methods=['GET'])
def get_all_characters():
    characters = Character.query.all()
    return jsonify([character.serialize() for character in characters]), 200


@api.route('/people/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Character.query.get(character_id)
    if character:
        return jsonify(character.serialize()), 200
    return jsonify({"error": "Personaje no encontrado"}), 404



# Rutas planetas #

@api.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200


@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        return jsonify(planet.serialize()), 200
    return jsonify({"error": "Planeta no encontrado"}), 404



# Rutas naves #

@api.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([vehicle.serialize() for vehicle in vehicles]), 200


@api.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle:
        return jsonify(vehicle.serialize()), 200
    return jsonify({"error": "Vehículo no encontrado"}), 404



# Rutas usuarios/favoritos

@api.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200


@api.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Se requiere User ID"}), 400

    favorites = Favorite.query.filter_by(user_id=user_id).all()
    if not favorites:
        return jsonify({"message": "No se encontraron favoritos para este usuario"}), 404

    return jsonify([fav.serialize() for fav in favorites]), 200


@api.route('/favorites/planet/<planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Se requiere User ID"}), 400

    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planeta no encontrado"}), 404
    
    existing_favorite = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if existing_favorite:
        return jsonify({"message": "Este planeta ya está en favoritos"}), 409

    favorite = Favorite(user_id=user_id, planet_id=planet.id)
    db.session.add(favorite)
    db.session.commit()

    return jsonify(favorite.serialize()), 201


@api.route('/favorites/people/<character_id>', methods=['POST'])
def add_favorite_character(character_id):
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Se requiere User ID"}), 400

    existing_favorite = Favorite.query.filter_by(user_id=user_id, character_id=character_id).first()
    if existing_favorite:
        return jsonify({"message": "Este personaje ya está en favoritos"}), 409

    character = Character.query.get(character_id)
    if not character:
        return jsonify({"error": "Personaje no encontrado"}), 404
    
    favorite = Favorite(user_id=user_id, character_id=character.id)
    db.session.add(favorite)
    db.session.commit()

    return jsonify(favorite.serialize()), 201


@api.route('/favorites/vehicle/<vehicle_id>', methods=['POST'])
def add_favorite_vehicle(vehicle_id):
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Se requiere User ID"}), 400

    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({"error": "Vehículo no encontrado"}), 404
    
    favorite = Favorite(user_id=user_id, vehicle_id=vehicle.id)
    db.session.add(favorite)
    db.session.commit()

    return jsonify(favorite.serialize()), 201


@api.route('/favorites/planet/<planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Se requiere User ID"}), 400

    favorite = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if not favorite:
        return jsonify({"error": "Favorito no encontrado"}), 404
    
    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"message": "Planeta favorito borrado exitosamente"}), 200


@api.route('/favorites/people/<character_id>', methods=['DELETE'])
def delete_favorite_character(character_id):
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Se requiere User ID"}), 400

    favorite = Favorite.query.filter_by(user_id=user_id, character_id=character_id).first()
    if not favorite:
        return jsonify({"error": "Personaje favorito no encontrado"}), 404
    
    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"message": "Personaje favorito borrado exitosamente"}), 200


@api.route('/favorites/vehicle/<vehicle_id>', methods=['DELETE'])
def delete_favorite_vehicle(vehicle_id):
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Se requiere User ID"}), 400

    favorite = Favorite.query.filter_by(user_id=user_id, vehicle_id=vehicle_id).first()
    if not favorite:
        return jsonify({"error": "Vehículo favorito no encontrado"}), 404
    
    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"message": "Vehículo favorito borrado exitosamente"}), 200
