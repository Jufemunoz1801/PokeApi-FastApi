import requests  # Importamos la librería requests, que nos permite hacer solicitudes HTTP en Python
    
class Pokemon:# Definimos la clase Pokemon, que representa un Pokémon
    def __init__(self, name):#definimos el contructor
        self.name = name# Asignamos el nombre del Pokémon al atributo "name" de la instancia de la clase
       
    def show(self):# Definimos un método llamado "show" que mostrará las habilidades del Pokémon
        url = requests.get('https://pokeapi.co/api/v1/pokemon/'+ self.name) # Hacemos una solicitud GET a la API de Pokémon para obtener información sobre el Pokémon con el nombre especificado
        if url.status_code == 200:# Verificamos si la solicitud fue exitosa (código de estado HTTP 200)
            response = url.json()#Nos retorna el archivo json
            abilities = [ability['ability']['name'] for ability in response['abilities']]# Extraemos las habilidades del Pokémon del diccionario de la respuesta y las almacenamos en una lista
            return f"Pokemon: {self.name.capitalize()}\nHabilidades: {', '.join(abilities)}"
        else:
            return f"El pokemon '{self.name}' no existe"