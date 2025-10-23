from google.adk.agents import Agent
from adeka.configs.main_config import *
from adeka.configs.ai_config import *
from adeka.tools.airxiv_tool import *


AGENT_DESCRIPTION = "An Agent that helps to explore arXiv site"
AGENT_INSTRUCTION = (
    "You are a helpful assistant. "
    "Your job is to fetch the latest papers from arXiv using the `search_latest_arxiv` tool. "
    "The user will provide a domain of anything from general to a specific subject as a publication can be related to any kind of field"
    "The user might also specify a number of papers to fetch (e.g., 'get 5 papers'). "
    "If they don't specify a number, use the tool's default."
    "When generating the response, make sure to include a concise explanation about the paper and the link"
)


root_agent = Agent(
    model=MODEL_NAME,
    name=AIRXIV_AGENT_NAME,
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    generate_content_config=CONFIG_1,
    tools=[search_latest_arxiv],
)