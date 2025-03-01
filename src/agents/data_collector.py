from agents.base_agent import BaseAgent
from smolagents.agents import ToolCallingAgent
from smolagents.default_tools import DuckDuckGoSearchTool
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


@tool
def tiktok_trending_hashtags(days: str) -> str:
    """
    Fetches trending TikTok hashtags in the USA for the past X days using the Apify TikTok Trending Hashtags Scraper.

    Args:
        days: A string representing the number of days to look back (e.g., "7" for 7 days).
    Returns:
        A JSON string containing the trending hashtags dataset.
    """
    apify_token = os.getenv("APIFY_TOKEN")
    if not apify_token:
        raise ValueError("APIFY_TOKEN environment variable not set.")

    # Initialize ApifyClient
    client = ApifyClient(apify_token)
    
    # Prepare actor input
    run_input = {
        "countryCode": "US",
        "maxItems": 40,
        "period": days  # e.g., "7" for 7 days
    }
    
    # Run the actor and wait for it to finish
    run = client.actor("YHnqz388prKDbPGFx").call(run_input=run_input)
    
    # Fetch results from the dataset
    dataset_items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    
    # Return as JSON string
    save_path = os.path.join(os.curdir, "data")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    data = json.dumps(dataset_items)
    file_path = os.path.join(save_path, "tiktok.json")
    
    with open(file_path, "w") as f:  # Use 'wb' for binary data
        f.write(data)
    return f"Saved data in {file_path}"


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
        tools = [download_tool, tiktok_trending_hashtags]
        super().__init__(**kwargs)
        super(ToolCallingAgent, self).__init__(model=self.model, tools=tools, max_steps=12, **kwargs)

        # This prompt frames the agent's role and behavior
        self.base_prompt = (f"""
            "You are the Data Collector Agent. Your job is to:
            Use the tools provided to find trending hashtags on TikTok.
            Store these trending hashtags in the /data folder.
            Download any files into the /data folder
            Use the internet to find data.
            """
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
<CONTEXT>
{context}
<\CONTEXT>
"""

        # The ToolCallingAgent's `run` method will parse the prompt,
        # potentially call tools, and return the final output.
        return self.run(prompt)
