# NOT USING THIS AGENT CURRENTLY

from agents.base_agent import BaseAgent
from smolagents.agents import ToolCallingAgent

class Presenter(BaseAgent, ToolCallingAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_prompt = f"""
        You are the presenter agent. You need to generate a final report based on data given to you by the developer agent..
        """

    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThese are the signals you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow generate a report from these signals."
        return self.run(prompt)
        