from common_agent.AgentTools.tool_init import initialize_agent_tools
from google.adk.tools import google_search


def create_translate_agent():
    description = """ The specialist agent for language translation (e.g., English-Vietnamese, Vietnamese-English). 
    Output is text in the target language. 
    Must not perform web searches or provide additional information beyond translation.
    
"""
    instruction = """
You are the impartial Translation Agent. 
Task: Accurately translate the input text. 
Show your translated_text only in the translated_text field when user did not require further information(ex. explanation, example,...).
When user want to show more information, you can use google search tool to find more information then show
explanation in short below
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