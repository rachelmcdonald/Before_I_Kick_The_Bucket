import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("Australia", True)
country_repository.save(country1)
country2 = Country("Italy", True)
country_repository.save(country2)

country_repository.select_all()

city1 = City("Perth", country1, True)
city_repository.save(city1)

city2 = City("Rome", country2, False)
city_repository.save(city2)


pdb.set_trace()