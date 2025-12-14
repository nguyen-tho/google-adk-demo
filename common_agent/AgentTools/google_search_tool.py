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
    The specialist agent for external information retrieval (Web Search Tool). 
    Output is a structured JSON object containing raw snippets and sources. 
    Must not translate or interpret the content found.
    """
    instruction = """    You are the objective Information Retrieval Agent. 
    Task: Use your Search Tool to answer the input query. 
    Mandatory Output Constraint: You must return a single JSON structure following this exact schema. 
    The search_snippets array must contain pairs of content (raw quote) and source (URL). 
    {"type": "search_result", "status": "success", "query": "[Search query]", "search_snippets":
    [{"content": "[Raw snippet content]", "source": "[URL]"}, {"content": "[Another raw snippet]", 
    "source": "[Another URL]"}]}. """
    google_search_agent = initialize_agent_tools(agent_name=agent_name,
                                                 model=model,
                                                 type=type,
                                                 description=description,
                                                 instruction=instruction,
                                                 tools=tools)
    return google_search_agent