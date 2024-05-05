import requests  # Import the library that allow us to create HTTP request
    
class Pokemon:# class definition
    def __init__(self, name):# constructor method
        self.name = name# attribute instantiation 
       
    def show(self):# method definition 
        url = requests.get('https://pokeapi.co/api/v1/pokemon/'+ self.name) # We make a GET request to the Pokémon API to get information about the Pokémon with the specified name.
        if url.status_code == 200:# We check if the request was successful (HTTP status code 200)
            response = url.json()#return the json a file
            abilities = [ability['ability']['name'] for ability in response['abilities']]# We extract the Pokémon's abilities from the dictionary of the response and store them in a list
            return f"Pokemon: {self.name.capitalize()}\nHabilidades: {', '.join(abilities)}"
        else:
            return f"El pokemon '{self.name}' no existe"