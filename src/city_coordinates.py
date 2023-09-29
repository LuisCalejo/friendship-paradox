from geopy.geocoders import Nominatim

# Initialize the geolocator
geolocator = Nominatim(user_agent="FriendshipParadoxApp")


# List of cities
cities = ['Westport', 'Cork', 'Belfast', 'Dublin', 'Faro', 'Porto', 'Lisbon', 'Santiago de Compostela', 'Santander', 'Pamplona', 'Seville', 'Málaga', 'Valencia', 'Madrid', 'Barcelona', 'Montpellier', 'Marseille', 'Nice', 'Catania', 'Bari', 'Naples', 'Rome', 'Florence', 'Bologna', 'Venice', 'Milan', 'Bern', 'Lyon', 'Bordeaux', 'Rennes', 'Istanbul', 'Stockholm', 'Amsterdam', 'Brussels', 'Cologne', 'Berlin', 'Hamburg', 'Copenhagen', 'Oslo', 'Östersund', 'Trondheim', 'Kiruna', 'Bergen', 'Frankfurt', 'Munich', 'Prague', 'Warsaw', 'Vienna', 'Budapest', 'Ljubljana', 'Zagreb', 'Split', 'Belgrade', 'Bucharest', 'Sofia', 'Skopje', 'Thessaloniki', 'Athens', 'Patras', 'Helsinki', 'Turku', 'Rovaniemi', 'Paris', 'London', 'Penzance', 'Bristol', 'Birmingham', 'Holyhead', 'Edinburgh', 'Glasgow', 'Aberdeen', 'Vilnius', 'Bialystok', 'Klaipėda', 'Riga', 'Tallinn', 'Ankara', 'Gdańsk', 'Poznań', 'Wrocław', 'Krakau']

# Fetch coordinates
def get_coordinates(city):
    location = geolocator.geocode(city)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

coordinates = {city: get_coordinates(city) for city in cities}

for city, coord in coordinates.items():
    print(f"{city}: {coord}")

x=1