from agents.base_agent import BaseAgent
from smolagents.agents import ToolCallingAgent
import os

class Reviewer(BaseAgent, ToolCallingAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data_location = os.path.join(os.curdir, "data")
        products_list = os.path.join(data_location, "consumer_products")
        self.base_prompt = f"""
        You are the reviewer agent. You will review the list of products in {products_list} and decide whether the list is good or not.
        A good list will contain individual branded products, not a category of products, for instance, "Nike Air Max" is an example of a product, "Sports shoes" is an example of a category.
        You need to decide whether it is good or not, by outputting \"yes\" or \"no\". 
        """
    
    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThis here is the context you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow decide whether this is a good list of products or not. Output \"yes\" or \"no\"."
        return self.run(prompt)
