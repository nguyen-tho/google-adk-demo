from common_agent.AgentTools.tool_init import initialize_agent_tools
from google.adk.tools import google_search


    
def create_translate_agent():
    description = """ You are a useful tool to translate text from one language to another.
You can set the source language and the destination language, and then translate the given text accordingly.
"""
    instruction = """ Use the Translator tool from the Google Search tool to translate text between languages as a professional translator and interpreter."""

    translator_agent = initialize_agent_tools(
    agent_name="TranslatorAgent",
    model="gemini-2.5-flash",
    type="llm",
    description=description,
    instruction=instruction,
    tools=[google_search]
    )
    return translator_agent