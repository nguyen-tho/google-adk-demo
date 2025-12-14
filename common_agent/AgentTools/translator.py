from common_agent.AgentTools.tool_init import initialize_agent_tools
from google.adk.tools import google_search


def create_translate_agent():
    description = """ The specialist agent for language translation (e.g., English-Vietnamese, Vietnamese-English). 
    Output is strictly a structured JSON object.
    Must not add explanations, comments, or any extraneous information beyond the direct translation.
"""
    instruction = """
You are the impartial Translation Agent. 
Task: Accurately translate the input text. 
Mandatory Output Constraint: You must return a single JSON structure following this exact schema.
No exceptions. {"type": "translation_result", "status": "success", 
"original_text": "[Original text]", "translated_text": "[Accurate translation]"}.
    """

    translator_agent = initialize_agent_tools(
    agent_name="TranslatorAgent",
    model="gemini-2.5-flash",
    type="llm",
    description=description,
    instruction=instruction,
    tools=[]
    )
    return translator_agent