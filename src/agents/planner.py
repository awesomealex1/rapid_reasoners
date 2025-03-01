from src.agents.base_agent import BaseAgent
from smolagents.agents import ToolCallingAgent

class Planner(BaseAgent, ToolCallingAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_prompt = "You are the planner agent. You are given a question that you need to create a plan for, that is then executed by a series of agents. You may be given additional context of previous agent calls. If that is the case, create another plan to improve upon the final result."
    
    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThis here is the context you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow create a plan which other agents can execute upon."
        return self.run(prompt)

