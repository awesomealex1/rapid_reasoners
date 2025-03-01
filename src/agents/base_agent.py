from smolagents.agents import MultiStepAgent
from smolagents.models import OpenAIServerModel
import os

class BaseAgent(MultiStepAgent):

    def __init__(self, **kwargs):
        model = OpenAIServerModel("gpt-4o-mini", "https://api.openai.com/v1", os.getenv("OPENAI_KEY"))
        super().__init__(tools=[], model=model)

    def execute(input, **kwargs):
        raise NotImplementedError("Need to implement execute method.")