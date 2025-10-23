from google.adk.agents import LlmAgent
from adeka.configs.main_config import *
from adeka.tools.wikipedai_tool import search_wikipedia_tool


AGENT_DESCRIPTION = """
An agent that finds and summarizes information from Wikipedia.
"""
AGENT_INSTRUCTION = """
When asked about a topic, search Wikipedia, extract relevant text, and summarize it clearly.
If the topic cannot be found, respond accordingly.
"""

root_agent = LlmAgent(
    model=MODEL_NAME,
    name=WIKIPEDAI_AGENT_NAME,
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    tools=[search_wikipedia_tool]
)