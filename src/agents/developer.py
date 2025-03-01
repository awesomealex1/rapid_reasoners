from agents.base_agent import BaseAgent
from smolagents.agents import CodeAgent

class Developer(BaseAgent, CodeAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_prompt = "You are the developer agent who is a professional data scientist. Analyse each file data folder one by one. The data folder is located at /data. Once you have accessed the data - print out all the data files to make sure you are using the right sources. For each file, conduct professional data science analysis as a professional signal processor and report any interesting signals you find. You can use any tools you like, but you must provide a clear explanation of the signals you find."
    
    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThis here is the context you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow create a solution."
        return self.run(prompt)
    
