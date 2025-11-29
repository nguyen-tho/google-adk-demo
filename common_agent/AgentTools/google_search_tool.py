from common_agent.AgentTools.tool_init import initialize_workflow_agent
from common_agent.AgentTools.tool_init import initialize_agent_tools
from google.adk.tools import google_search

def create_google_search_agent(model: str = "gemini-2.5-flash", type: str = "agent"):
    """
    Create a Google Search agent with the specified parameters.

    Args:
        agent_name (str): The name of the agent.
        model (str, optional): The model to be used by the agent. Defaults to "gemini-2.5-flash".
        type (str, optional): The type of agent. Defaults to "agent".
        description (str, optional): Description of the agent. Defaults to "".
        instruction (str, optional): Instructions for the agent. Defaults to "".
    Returns:
        Agent: The initialized Google Search agent.
    """
    agent_name = "GoogleSearchAgent"
    tools = [google_search]
    description = """
    An agent that uses Google Search to answer questions.
    It can search the web for information and provide accurate answers based on the search results.
    """
    instruction = """    You are a helpful assistant that answers questions using Google Search.
    Use the Google Search tool to find relevant information and provide accurate answers.
    Always cite your sources from the search results. """
    google_search_agent = initialize_agent_tools(agent_name=agent_name,
                                                 model=model,
                                                 type=type,
                                                 description=description,
                                                 instruction=instruction,
                                                 tools=tools)
    return google_search_agent