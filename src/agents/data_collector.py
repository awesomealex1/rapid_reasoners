from agents.base_agent import BaseAgent
from smolagents.agents import ToolCallingAgent
from smolagents.default_tools import DuckDuckGoSearchTool
from smolagents import tool
import urllib
import os

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

class DataCollector(BaseAgent, ToolCallingAgent):
    """
    The DataCollector agent takes a plan (prompt) from the Planner,
    then uses various search tools (Reddit, Google Trends, public datasets, etc.)
    to gather relevant data sources iteratively. 
    Finally, it outputs a list of potential data sources for the Interpreter.
    """

    def __init__(self, **kwargs):
        # If you have real tool classes, add them to the list below
        # e.g. tools = [RedditSearchTool(), GoogleTrendsTool(), PublicDatasetSearchTool()]
        tools = [DuckDuckGoSearchTool(), download_tool]
        super().__init__(**kwargs)
        super(ToolCallingAgent, self).__init__(model=self.model, tools=tools, **kwargs)

        # This prompt frames the agent's role and behavior
        self.base_prompt = (
            "You are the Data Collector Agent. Your job is to:\n"
            "Download any files into the /data folder\n"
            "Use the internet to find data.\n"
        )

    def execute(self, context, **kwargs):
        """
        Iteratively collects data sources based on the plan from the Planner Agent.
        The final output should be a structured list or description of data sources.
        """
        
        # Construct a single prompt instructing the agent to do multiple steps
        # If you'd like multiple calls/steps, you can do that as well—this is a minimal example.
        prompt = f"""
{self.base_prompt}
The context you have been given is:
---
{context}
"""

        # The ToolCallingAgent's `run` method will parse the prompt,
        # potentially call tools, and return the final output.
        return self.run(prompt)
