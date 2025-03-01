from smolagents import CodeAgent, tool
from smolagents.models import OpenAIServerModel
import os
from apify_client import ApifyClient

# Define the TikTok Trending Hashtags Tool using ApifyClient
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
        "maxItems": 100,
        "period": days  # e.g., "7" for 7 days
    }
    
    # Run the actor and wait for it to finish
    run = client.actor("YHnqz388prKDbPGFx").call(run_input=run_input)
    
    # Fetch results from the dataset
    dataset_items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    
    # Return as JSON string
    import json
    return json.dumps(dataset_items)

class Developer(CodeAgent):
    def __init__(self, **kwargs):
        model = OpenAIServerModel("gpt-4o-mini", "https://api.openai.com/v1", os.getenv("OPENAI_KEY"))
        super().__init__(
            tools=[tiktok_trending_hashtags],
            model=model,
            additional_authorized_imports=[
                "numpy", "pandas", "json", "csv", "os", "glob", "markdown", 
                "requests", "bs4"  # Added bs4 for HTML parsing
            ]
        )
        data_location = os.path.join(os.curdir, "data")
        self.base_prompt = f"""
You are the Developer Agent, a professional data scientist tasked with identifying trending consumer product hashtags on TikTok that could impact publicly traded companies. Use the `tiktok_trending_hashtags` tool to fetch trending hashtags in the USA for the past X days (e.g., '7' for 7 days). Analyze the dataset to find signals of significant consumer trends, focusing on:
- Hashtag name and video views (magnitude of trend).
- Public posts count (engagement).
- Rank and industry info (relevance).
Parse the JSON output with `json.loads()` and use pandas for analysis if needed. Report interesting signals with clear explanations.

Additionally, analyze local data files in the folder `{data_location}` if provided. Use `bs4` (BeautifulSoup) to parse HTML files and extract consumer product trends. Print all data sources used and combine insights from TikTok and local files to identify potential impacts on publicly traded companies.
"""
        self.python_executor.static_tools.update({"open": open})
    
    def execute(self, input, **kwargs):
        prompt = self.base_prompt + "\nThis here is the context you have been given: <CONTEXT>\n" + input + "<\CONTEXT>\nNow create a solution."
        return self.run(prompt)

# Example usage
if __name__ == "__main__":
    developer = Developer()
    result = developer.execute("Fetch and analyze trending TikTok hashtags in the USA for the past 7 days, and combine with local data analysis.")
    print(result)