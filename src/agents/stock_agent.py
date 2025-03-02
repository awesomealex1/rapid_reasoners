from agents.base_agent import BaseAgent
from smolagents.agents import CodeAgent
from smolagents.default_tools import DuckDuckGoSearchTool
from smolagents.models import OpenAIServerModel
from smolagents import tool
import urllib
import os
from apify_client import ApifyClient
import json


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

class StockPicker(CodeAgent):

    def __init__(self, **kwargs):
        tools = [DuckDuckGoSearchTool(), download_tool]
        model = OpenAIServerModel("gpt-4o-mini", "https://api.openai.com/v1", os.getenv("OPENAI_KEY"))
        super().__init__(tools=tools, model=model, additional_authorized_imports=["requests", "numpy", "pandas", "json", "csv", "os", "glob", "markdown"])
        data_location = os.path.join(os.curdir, "data")
        supply_chains = os.path.join(data_location, "supply_chain")
        stocks = os.path.join(data_location, "stocks.txt")
        self.base_prompt = f"""
        You are the stock picker agent. You will be given a list of supply chains in {supply_chains} and then need to find out about stocks to invest in based on these supply chains. Use the internet to find related stocks.
        A good list of stock will contain stock tickers and at least 5 different stocks. It will not contain links. Output the final list to {stocks}
        """
        self.python_executor.static_tools.update({"open": open})
    
    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThis here is the context you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow create a list of stocks based on this context."
        return self.run(prompt)
