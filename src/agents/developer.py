from agents.base_agent import BaseAgent
from smolagents.agents import CodeAgent

class Developer(BaseAgent, CodeAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_prompt = "You are the developer agent. You are given a plan and need to code a solution."
    
    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThis here is the context you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow create a solution."
        return self.run(prompt)
