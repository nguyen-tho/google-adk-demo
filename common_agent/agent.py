from google.adk.agents.llm_agent import Agent, LlmAgent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.sequential_agent import SequentialAgent
import common_agent.AgentTools.timezone as tz_module
import common_agent.AgentTools.location as loc_module
import common_agent.AgentTools.weather as weather_module
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search


def get_current_time(city_name: str) -> str:
    """
    Get the current time in the specified city.

    Args:
        city_name (str): The name of the city.
    Returns:
        str: The current time in the specified city formatted as "YYYY-MM-DD HH:MM:SS".
    """
    try:
        location = tz_module.TimeZoneLocation(city_name)
        current_time = location.get_current_time_in_city()
        return {"status": "success", "city": city_name, "time": current_time}
    except ValueError as e:
        return {"status": "error", "message": str(e)}

def get_location_coordinates(city_name: str, to_dms: bool) -> tuple:
    """
    Get the latitude and longitude of the specified city.

    Args:
        city_name (str): The name of the city.
    Returns:
        tuple: A tuple containing the latitude and longitude of the city.
    """
    try:
        location = loc_module.Location(city_name)
        lat, lon = location.get_location_based_on_city()
        if to_dms:
            lat = location.float_to_DMS(lat, is_latitude=True)
            lon = location.float_to_DMS(lon, is_latitude=False)
        return {"status": "success", "city": city_name, "coordinates": {"latitude": lat, "longitude": lon}}
    except ValueError as e:
        return {"status": "error", "message": str(e)}
def get_location_timezone(city_name: str) -> str:
    """
    Get the timezone of the specified city.

    Args:
        city_name (str): The name of the city.
    Returns:
        str: The timezone of the specified city.
    """
    try:
        location = tz_module.TimeZoneLocation(city_name)
        timezone_str = location.get_timezone_based_on_city()
        return {"status": "success", "city": city_name, "timezone": timezone_str}
    except ValueError as e:
        return {"status": "error", "message": str(e)}

#weather tool 
def get_current_weather(city_name: str, unit: str) -> dict:
    """
    Get the current weather for the specified city.

    Args:
        city_name (str): The name of the city.
        unit (str, optional): The unit of measurement for temperature. Defaults to "metric".
            there are some units: ["default/None", "metric", "imperial"].
            with default unit is Kelvin, metric is Celsius, imperial is Fahrenheit.
    Returns:
        dict: A dictionary containing the weather information, or an error message if not found.
    """
    weather_tool = weather_module.WeatherTool(city_name)
    weather_info = weather_tool.get_current_weather(unit)
    if weather_info:
        return {"status": "success", "weather": weather_info}
    else:
        return {"status": "error", "message": f"City '{city_name}' Not Found or Invalid API Key."}
# Define the root agent with the above tools
common_subagent = Agent(
    model='gemini-2.0-flash',
    name='common_tools_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time, location coordinate, timezone, and weather in cities.",
    tools=[get_current_time, get_location_coordinates, get_location_timezone, get_current_weather],
)

google_subagent = Agent(
        name="basic_search_agent",
        model="gemini-2.0-flash",
        description="Agent to answer questions using Google Search.",
        instruction="I can answer your questions by searching the internet. Just ask me anything!",
        # google_search is a pre-built tool which allows the agent to perform Google searches.
        tools=[google_search])

parallel_agents = ParallelAgent(
    name="common_google_agent",
    description="An agent that combines common tools and Google Search capabilities.",
    sub_agents=[common_subagent, google_subagent])

#merger agent is a LlmAgent that takes the outputs of the parallel agent and synthesizes them.
merger_agent = LlmAgent(
    name="SynthesisAgent",
    model="gemini-2.0-flash",
    description="An agent that synthesizes the results from the parallel research agent.",
    instruction="You synthesize the information gathered by the parallel agent to provide a comprehensive answer.",
)

sequential_pipeline_agent  = SequentialAgent(
     name="root_agent",
     # Run parallel research first, then merge
     sub_agents=[parallel_agents, merger_agent],
     description="Coordinates parallel research and synthesizes the results."
 )

root_agent = sequential_pipeline_agent