import os
from dotenv import load_dotenv
load_dotenv()

MODEL_NAME=os.getenv("MODEL_NAME")

MODEL_NAME=os.getenv("MODEL_NAME")
GENERAL_AGENT_NAME=os.getenv("GENERAL_AGENT_NAME", "GeneralAI")
WIKIPEDAI_AGENT_NAME=os.getenv("WIKIPEDAI_AGENT_NAME", "WikipedAI")
AIRXIV_AGENT_NAME=os.getenv("AIRXIV_AGENT_NAME", "AIrxiv")