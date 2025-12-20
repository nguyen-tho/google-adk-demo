from google.adk.tools.agent_tool import AgentTool
from common_agent.AgentTools.tool_init import initialize_workflow_agent, initialize_agent_tools
from common_agent.AgentTools.google_search_tool import create_google_search_agent
from common_agent.AgentTools.translator import create_translate_agent
from common_agent.AgentTools.multiple_tool import create_multiple_common_tool_agent

# Initialize sub-agents
search_agent = create_google_search_agent()
translator_agent = create_translate_agent()
common_tool_agent = create_multiple_common_tool_agent()
# Initialize a LLM model to merge all sub-agents
root_agent = initialize_agent_tools(
    agent_name="root_agent",
    model="gemini-2.5-flash",
    tools=[AgentTool(search_agent), AgentTool(translator_agent)],
    description="The root agent that uses search and translator agents to handle user queries.",
    instruction="You are the root agent. Use the available tools to assist with user queries."
)