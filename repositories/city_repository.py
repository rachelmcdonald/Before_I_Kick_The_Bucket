from db.run_sql import run_sql
from models.city import City
from models.country import Country
from repositories import country_repository


def save(city):
    sql = "INSERT INTO cities(name, visited, country_id) VALUES ( %s, %s, %s ) RETURNING id"
    values = [city.name, city.visited, city.country.id]
    results = run_sql( sql, values )
    city.id = results[0]['id']
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['id'])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    country = country_repository.select(result['country_id'])

    if result is not None:
        city = City(result['name'], country, result['visited'], result['id'] )
    return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
    sql = "UPDATE cities SET (name, visited, country_id) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.visited, city.country.id, city.id]
    run_sql(sql, values)

def cities(city):
    cities = []

    sql = "SELECT * FROM cities WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['city'], row['visited'], row['id'] )
        cities.append(city)
    return cities