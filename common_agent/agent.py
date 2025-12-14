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
    description="""The high-level coordinating agent. 
    Specializes in analyzing user intent, strategically distributing tasks to sub-agents (Translation, Search),
    and synthesizing their structured JSON outputs into a single, cohesive, and natural language response.""",
    instruction="""You are a professional Orchestrator Agent. 
    1. Analyze: Evaluate the user's request to determine if both Translation and Search are required. 
    2. Distribute: Send the exact text requiring translation to the Translation Agent and the specific question requiring information retrieval to the Search Tool Agent.
    3. Synthesize: Upon receiving the structured JSON outputs from the sub-agents, check the type and status fields. 
    You must merge the translated_text and the search_snippets into one final, coherent, non-redundant, and fluent answer for the user.""",
)

# create pipeline workflow agent
parallel_agents = initialize_workflow_agent(
    agent_name="ParallelAgentsWorkflow",
    workflow_type="parallel",
    sub_agents=[search_agent, translator_agent]
)

agent_pipeline = synthesis_agent(
    agent_name="root_agent",
    parallel_agent=parallel_agents,
    sequential_agent=merge_agent
)

#root agent is agent_pipeline
root_agent = agent_pipeline