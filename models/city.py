from models.country import Country


class City:

    def __init__(self, name, country_id, visited = False, id = None,):
        self.name = name
        self.country_id = country_id
        self.visited = visited
        self.country = Country
        self.id = id

    def mark_visit(self):
        self.visited = True