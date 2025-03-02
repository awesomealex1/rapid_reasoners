from agents.base_agent import BaseAgent
from smolagents.agents import CodeAgent
from smolagents import tool
from smolagents.models import OpenAIServerModel
import os
from smolagents.default_tools import DuckDuckGoSearchTool, GoogleSearchTool

@tool
def download_tool(url: str, file_name: str) -> str:
    """
    This is a download tool.

    Args:
        url: url from which to download
        file_name: the name of the file that you want to save
    """
    # Download the data from the URL
    
    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, None, headers)  # The assembled request
    response = urllib.request.urlopen(request)
    data = response.read()  # The data you need
    
    # Ensure the directory exists
    save_path = os.path.join(os.curdir, "data")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    # Save the data to the file
    file_path = os.path.join(save_path, file_name)
    
    with open(file_path, "wb") as f:  # Use 'wb' for binary data
        f.write(data)

    return f"Downloaded and saved as {file_path}."  # Return the saved file path

class Developer(CodeAgent):

    def __init__(self, **kwargs):
        tools = [DuckDuckGoSearchTool(), download_tool]
        model = OpenAIServerModel("gpt-4o-mini", "https://api.openai.com/v1", os.getenv("OPENAI_KEY"))
        super().__init__(tools=tools, model=model, additional_authorized_imports=["requests", "numpy", "pandas", "json", "csv", "os", "glob", "markdown"])
        data_location = os.path.join(os.curdir, "data")
        consumer_data_folder = os.path.join(data_location, "consumer_data")
        self.base_prompt = f"""
        You are the developer agent who is a professional data scientist.
        You will use only the trending labels stored in {data_location} to search the web for consumer products that relate to the trending labels in {data_location}.
        Download the comsumer product data you find, including the urls, create a folder called {consumer_data_folder} and store the consumer data in it.
        You can use any tools you like, but you must store the consumer product data you find in a .txt file in {consumer_data_folder} folder. Ensure the data is readable, i.e. do not put one character on each line.
        When you use the web_search method, sleep 10 seconds inbetween each call to avoid a timeout.
        """
        self.python_executor.static_tools.update({"open": open})
    
    def execute(self, context, **kwargs):
        prompt = f"""
        {self.base_prompt}
         This here is the context you have been given: 
         <CONTEXT>
         {context}
         <\CONTEXT>
         """
        return self.run(prompt)