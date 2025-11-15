from geopy.geocoders import Nominatim


class Location: 
    def __init__(self, city_name: str):
        self.city_name = city_name
        self.latitude = 0.0
        self.longitude = 0.0
        
    def set_coordinates(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self):
        return self.latitude, self.longitude
    
    def get_city_name(self):
        return self.city_name

    def set_city_name(self, city_name: str):
        self.city_name = city_name
        
    def float_to_DMS(self, decimal_degree: float, is_latitude: bool):
        degrees = int(decimal_degree)
        minutes_float = abs(decimal_degree - degrees) * 60
        minutes = int(minutes_float)
        seconds = (minutes_float - minutes) * 60
        direction = ''
        if is_latitude:
            direction = 'N' if decimal_degree >= 0 else 'S'
        else:
            direction = 'E' if decimal_degree >= 0 else 'W'
        return f"{abs(degrees)}°{minutes}'{seconds:.2f}\" {direction}"
         
    def get_location_based_on_city(self):
        geolocator = Nominatim(user_agent="timezone_agent")
        location = geolocator.geocode(self.city_name)
        if location:
            self.set_coordinates(location.latitude, location.longitude)
            return location.latitude, location.longitude
        else:
            raise ValueError(f"Could not find location for city: {self.city_name}")
        
    def get_city_based_on_location(self, latitude: float, longitude: float):
        geolocator = Nominatim(user_agent="timezone_agent")
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        if location and 'city' in location.raw['address']:
            city_name = location.raw['address']['city']
            self.set_city_name(city_name)
            return city_name
        else:
            raise ValueError(f"Could not find city for coordinates: ({latitude}, {longitude})")