from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from repositories import country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

# NEW city
# GET method with route looking like '/tasks/new'
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", countries = countries)

# CREATE a city
# POST method with route looking like '/tasks'
@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
   name = request.form['name']
   visited  = request.form['visited']
   country = country_repository.select(request.form['country_id'])
   city  = City(name, country, visited)
   city_repository.save(city)
   return redirect('/cities') 

# SHOW a city by its 'id'
# GET method
@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repository.select(id)
    return render_template("cities/show.html", city=city)

# EDIT a city
# GET method
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    countries = country_repository.select_all()
    city = city_repository.select(id)
    return render_template('cities/edit.html', city = city, countries = countries)

# UPDATE a city
# PUT method with route looking like '/tasks/<id>'
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited, id)
    city_repository.update(city)
    return redirect('/cities')  

# DELETE a city
# POST method with route looking like '/tasks/<id>'
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    print(f"Delete{id}")
    return redirect('/cities')