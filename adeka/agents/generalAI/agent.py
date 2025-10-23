from adeka.configs.main_config import *
from adeka.configs.ai_config import *
from google.adk.agents import LlmAgent

AGENT_DESCRIPTION = "A general-purpose AI that answers questions using built-in knowledge."
AGENT_INSTRUCTION = "Answer general questions as helpfully and accurately as possible."

root_agent = LlmAgent(
    model=MODEL_NAME,
    name=GENERAL_AGENT_NAME,
    description=AGENT_DESCRIPTION,
    generate_content_config=CONFIG_2,
    instruction=AGENT_INSTRUCTION,
)