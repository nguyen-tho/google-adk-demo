from timezonefinder import TimezoneFinder
from datetime import datetime
from zoneinfo import ZoneInfo
from common_agent.AgentTools.location import Location   
        
    
class TimeZoneLocation(Location):
    """
    A class to handle timezone and location functionalities based on city names.
    Inherits from Location class.
    """
    def __init__(self, city_name: str):
        super().__init__(city_name)
        self.timezone = ""
        self.current_time = ""
        
    def get_timezone(self):
        return self.timezone
    
    def set_timezone(self, timezone: str):
        self.timezone = timezone
        
    def set_current_time(self, current_time: str):
        self.current_time = current_time
        
    def get_current_time(self):
        return self.current_time
    
    def get_current_time_in_city(self, format = "%Y-%m-%d %H:%M:%S"):
        timezone_str = self.get_timezone_based_on_city()
        tz = ZoneInfo(timezone_str)
        current_time = datetime.now(tz)
        return current_time.strftime(format)

    def get_timezone_based_on_city(self):
        lat, lon = self.get_location_based_on_city()
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=lon, lat=lat)
        if timezone_str:
            return timezone_str
        else:
            raise ValueError(f"Could not determine timezone for city: {self.city_name}")
    

