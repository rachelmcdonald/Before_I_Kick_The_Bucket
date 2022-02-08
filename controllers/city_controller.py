from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() # NEW
    return render_template("cities/index.html", cities = cities)

@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repository.select(id)
    return render_template("cities/show.html", city=city)

@cities_blueprint.route("/city/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    return render_template('city/edit.html', city = city)

 # PUT '/tasks/<id>'
@cities_blueprint.route("/city/<id>", methods=['POST'])
def update_city(id):
    location = request.form['location']
    visited  = request.form['visited']
    city  = City(location, visited)
    city_repository.update(city)
    return redirect('/city')  

# NEW
# GET '/tasks/new'
@cities_blueprint.route("/city/new", methods=['GET'])
def new_city():
    cities = city_repository.select_all()
    return render_template("city/new.html", all_cities = cities)


# CREATE
# POST '/tasks'
@cities_blueprint.route("/city",  methods=['POST'])
def create_city():
   newcity = request.form['newcity']
   visited  = request.form['visited']
   city  = City(newcity, visited)
   city_repository.save(city)
   return redirect('/city') 


# DELETE
# DELETE '/tasks/<id>'
@cities_blueprint.route("/city/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/city')