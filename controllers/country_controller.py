from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("country", __name__)

@countries_blueprint.route("/country")
def countries():
    countries = country_repository.select_all() # NEW
    return render_template("country/index.html", countries = countries)

@countries_blueprint.route("/country/<id>")
def show(id):
    country = country_repository.select(id)
    return render_template("country/show.html", country=country)

@countries_blueprint.route("/country/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('country/edit.html', country = country)

 # PUT '/tasks/<id>'
@countries_blueprint.route("/country/<id>", methods=['POST'])
def update_country(id):
    location = request.form['location']
    visited  = request.form['visited']
    country  = Country(location, visited)
    country_repository.update(country)
    return redirect('/country')  

# NEW
# GET '/tasks/new'
@countries_blueprint.route("/country/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("country/new.html", all_countries = countries)


# CREATE
# POST '/tasks'
@countries_blueprint.route("/country",  methods=['POST'])
def create_country():
   newcountry = request.form['newcountry']
   visited  = request.form['visited']
   country  = Country(newcountry, visited)
   country_repository.save(country)
   return redirect('/country') 


# DELETE
# DELETE '/tasks/<id>'
@countries_blueprint.route("/country/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    print(f"Delete{id}")
    return redirect('/country')

