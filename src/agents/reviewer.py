from agents.base_agent import BaseAgent
from smolagents.agents import ToolCallingAgent
import os

class Reviewer(BaseAgent, ToolCallingAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data_location = os.path.join(os.curdir, "data")
        stocks_list = os.path.join(data_location, "stocks")
        self.base_prompt = f"""
        You are the reviewer agent. You will review the list of stocks in {stocks_list} and decide whether the list is good or not.
        A good list will contain stock stickers.
        You need to decide whether it is good or not, by outputting \"yes\" or \"no\". 
        """
    
    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThis here is the context you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow decide whether this is a good list of stocks or not. Output \"yes\" or \"no\"."
        return self.run(prompt)
