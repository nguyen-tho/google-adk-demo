# import module to initialize tools
from xml.parsers.expat import model
from google.adk.agents.llm_agent import LlmAgent, Agent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.loop_agent import LoopAgent

# Initialize the agent with necessary tools
def initialize_agent_tools(agent_name, model="gemini-2.5-flash", type="agent", description="", instruction="", tools=[]) -> Agent:
    """
    Initialize the agent with necessary tools.

    Args:
        agent_name (str): The name of the agent. 
        model (str, optional): The model to be used by the agent. Defaults to "gemini-2.5-flash".
        type (str, optional): The type of agent. Defaults to "agent" as a normal agent.
                            You can use 'llm' for LLM agent.
        description (str, optional): Description of the agent. Defaults to "".
        instruction (str, optional): Instructions for the agent. Defaults to "".
        tools (list, optional): List of tools to be added to the agent. Defaults to [].
    Returns:
        Agent: The initialized agent with the specified tools.
    """
    # Example: Add a Google Search tool
    if type.lower() == "agent":
        agent = Agent(name=agent_name, 
                         model=model,
                         description=description,
                         instruction=instruction,
                         tools=tools)
    elif type.lower() == "llm":
        agent = LlmAgent(name=agent_name, 
                      model=model,
                      description=description,
                      instruction=instruction,
                      tools=tools)
    else:
        raise ValueError(f"Invalid agent type: {type}. Choose from ['agent', 'llm'].")
    return agent

# Initialize agent with workflow.
# There are some types of workflow agents: ["Parallel", "Sequential", "Loop"]
def initialize_workflow_agent(agent_name, workflow_type="Sequential", sub_agents=[], description="") -> Agent:
    """
    Initialize a workflow agent with specified sub-agents.

    Args:
        agent_name (str): The name of the workflow agent.
        workflow_type (str, optional): The type of workflow agent. Defaults to "Parallel".
                                       Options are "Parallel", "Sequential", "Loop".
        sub_agents (list, optional): List of sub-agents to be included in the workflow. Defaults to [].
        description (str, optional): Description of the agent. Defaults to "".
    Returns:
        Agent: The initialized workflow agent with the specified sub-agents.
    """
    if workflow_type.lower() == "parallel":
        workflow_agent = ParallelAgent(name=agent_name,   
                                       description=description,
                                       sub_agents=sub_agents)
    elif workflow_type.lower() == "sequential":
        workflow_agent = SequentialAgent(name=agent_name,
                                         description=description,
                                         sub_agents=sub_agents)
    elif workflow_type.lower() == "loop":
        workflow_agent = LoopAgent(name=agent_name,
                                   description=description,
                                   sub_agents=sub_agents)
    else:
        raise ValueError(f"Invalid workflow type: {workflow_type}. Choose from ['Parallel', 'Sequential', 'Loop'].")
    
    return workflow_agent

# Synthesize two agents into a new SequentialAgent as a pipeline.
def synthesis_agent(parallel_agent: ParallelAgent, sequential_agent: SequentialAgent, agent_name) -> SequentialAgent:
    """
    Synthesize a new SequentialAgent that first runs a ParallelAgent and then a SequentialAgent.

    Args:
        parallel_agent (ParallelAgent): The ParallelAgent to run first.
        sequential_agent (SequentialAgent): The SequentialAgent to run after the ParallelAgent.

    Returns:
        SequentialAgent: A new SequentialAgent that combines the two agents.
    """
    synthesized_agent = initialize_workflow_agent(workflow_type="sequential",
        agent_name=agent_name,
        description="An agent that first runs a parallel agent followed by a sequential agent.",
        sub_agents=[parallel_agent, sequential_agent]
    )
    return synthesized_agent

def agent_hierachy(sub_agents: list[Agent], agent_name, description, model ='gemini-2.5-flash') ->LlmAgent:
    """
    Create a hierarchical LlmAgent that manages multiple sub-agents.

    Args:
        sub_agents (list[Agent]): List of sub-agents to be managed by the hierarchical agent.

    Returns:
        LlmAgent: A hierarchical LlmAgent that oversees the sub-agents.
    """
    hierachy_agent = LlmAgent(
        name=agent_name,
        model=model,
        description=description,
        sub_agents=sub_agents
    )
    return hierachy_agent


