from os import name


class Animals:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def display_info(self):
            print(self.nombre)    

class Lion(Animals):
    def __init__(self, nombre):
        super().__init__(nombre)
        
class Tigre(Animals):
    def __init__(self, nombre):
        super().__init__(nombre)
        
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def add_lion(self, name):
        self.animals.append( Lion(name) )
        
    def add_tiger(self, name):
        self.animals.append( Tigre(name) )
    
    
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            
zoo1 = Zoo("Pancho's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info() 