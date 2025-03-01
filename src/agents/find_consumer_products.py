from agents.base_agent import BaseAgent
from smolagents.agents import CodeAgent
from smolagents import tool
from smolagents.models import OpenAIServerModel
import os
from smolagents.default_tools import DuckDuckGoSearchTool

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

class ProductDeveloper(CodeAgent):

    def __init__(self, **kwargs):
        tools = [DuckDuckGoSearchTool(), download_tool]
        model = OpenAIServerModel("gpt-4o-mini", "https://api.openai.com/v1", os.getenv("OPENAI_KEY"))
        super().__init__(tools=tools, model=model, additional_authorized_imports=["requests", "numpy", "pandas", "json", "csv", "os", "glob", "markdown"])
        data_location = os.path.join(os.curdir, "data")
        consumer_data_folder = os.path.join(data_location, "consumer_data")
        consumer_products_folder = os.path.join(data_location, "consumer_products")
        self.base_prompt = f"""
        You will take the data stored in {consumer_data_folder} and search the web to create a list of consumer products related to the data.
        The product should be individual branded products, not a category of products, for instance, "Nike Air Max" is an example of a product, "Sports shoes" is an example of a category.
        You will store this list in the {consumer_products_folder} folder. Make sure it is a well formatted list of consumer products.
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