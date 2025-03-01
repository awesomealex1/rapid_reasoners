from agents.base_agent import BaseAgent
from smolagents.agents import CodeAgent
from smolagents.models import OpenAIServerModel
import os

class Developer(CodeAgent):

    def __init__(self, **kwargs):
        model = OpenAIServerModel("gpt-4o-mini", "https://api.openai.com/v1", os.getenv("OPENAI_KEY"))
        super().__init__(tools=[], model=model, additional_authorized_imports=["numpy", "pandas", "json", "csv", "os", "glob", "markdown"])
        data_location = os.path.join(os.curdir, "data")
        self.base_prompt = f"You are the developer agent who is a professional data scientist. Analyse each file data folder one by one. The data folder is located at {data_location}. Once you have accessed the data - print out all the data files to make sure you are using the right sources. For each file, conduct professional data science analysis as a professional signal processor and report any interesting signals you find. You can use any tools you like, but you must provide a clear explanation of the signals you find."
        self.python_executor.static_tools.update({"open": open})
    
    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThis here is the context you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow create a solution."
        return self.run(prompt)
    
