from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from repositories import country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() # NEW
    return render_template("cities/index.html", cities = cities)


# NEW
# GET '/tasks/new'
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    cities = city_repository.select_all()
    return render_template("cities/new.html", cities = cities)


# CREATE
# POST '/tasks'
@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
   newcity = request.form['newcity']
   visited  = request.form['visited']
   city  = City(newcity, visited)
   city_repository.save(city)
   return redirect('/cities') 

# SHOW
# GET
@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repository.select(id)
    return render_template("cities/show.html", city=city)

# EDIT
# GET
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    return render_template('cities/edit.html', city = city)

# UPDATE
# PUT '/tasks/<id>'
@cities_blueprint.route("/cities/<id>/edit", methods=['POST'])
def update_city(id):
    location = request.form['location']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(location, country, visited, id)
    city_repository.update(city)
    return redirect('/cities')  


# DELETE
# DELETE '/tasks/<id>'
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    print(f"Delete{id}")
    return redirect('/cities')