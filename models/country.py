class Country:
    def __init__(self, name, visited, id = None):
        self.name = name
        self.visited = visited
        self.id = id

    def mark_visit(self):
        self.visited = True