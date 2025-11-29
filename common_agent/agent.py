from common_agent.AgentTools.tool_init import initialize_workflow_agent, initialize_agent_tools, synthesis_agent
from common_agent.AgentTools.google_search_tool import create_google_search_agent
from common_agent.AgentTools.translator import create_translate_agent
from common_agent.AgentTools.multiple_tool import create_multiple_common_tool_agent

# Initialize sub-agents
search_agent = create_google_search_agent()
translator_agent = create_translate_agent()
common_tool_agent = create_multiple_common_tool_agent()
# Initialize a LLM model to merge all sub-agents
merge_agent = initialize_agent_tools(
    agent_name="MergeAgent",
    model="gemini-2.5-flash",
    type="llm",
    description="An agent to merge results from multiple sub-agents.",
    instruction="You are an expert at synthesizing information from various sources to provide comprehensive answers.",
)

# create pipeline workflow agent
parallel_agents = initialize_workflow_agent(
    agent_name="ParallelAgentsWorkflow",
    workflow_type="parallel",
    sub_agents=[search_agent, translator_agent, common_tool_agent]
)

agent_pipeline = synthesis_agent(
    agent_name="root_agent",
    parallel_agent=parallel_agents,
    sequential_agent=merge_agent
)

#root agent is agent_pipeline
root_agent = agent_pipeline