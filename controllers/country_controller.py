from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("country", __name__)

@countries_blueprint.route("/country")
def countries():
    countries = country_repository.select_all()
    return render_template("country/index.html", countries = countries)

@countries_blueprint.route("/country/<id>")
def show(id):
    country = country_repository.select(id)
    return render_template("country/show.html", country=country)

@countries_blueprint.route("/country/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('country/edit.html', country = country)

 # PUT method with route looking like '/tasks/<id>'
@countries_blueprint.route("/country/<id>", methods=['POST'])
def update_country(id):
    name = request.form['name']
    visited  = request.form['visited']
    country  = Country(name, visited, id)
    country_repository.update(country)
    return redirect('/country')  

# NEW country
# GET method with route looking like '/tasks/new'
@countries_blueprint.route("/country/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("country/new.html", all_countries = countries)

# CREATE a country
# POST method with route looking like '/tasks'
@countries_blueprint.route("/country",  methods=['POST'])
def create_country():
   newcountry = request.form['newcountry']
   visited  = request.form['visited']
   country  = Country(newcountry, visited)
   country_repository.save(country)
   return redirect('/country') 

# DELETE a country
# DELETE method with route looking like '/tasks/<id>'
@countries_blueprint.route("/country/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    print(f"Delete{id}")
    return redirect('/country')