# Earnings Day Stock Movement Prediction with Multi-Agent System

This project, developed for a hackathon, leverages a multi-agent system to predict stock price movements based trends. Built using the [Hugging Face SmolAgents framework](https://huggingface.co/docs/smolagents/en/index), it analyzes social data (e.g., TikTok trends) from which it find consumer products and their related supply chains. Based on these supply chains it picks stocks to then invest in.

## Our inspiration: The Slime Example
Since Q3 2023, the TikTok hashtag `#slime` has surged to 107M views and 16K posts, signaling a slime-making craze. Slime’s key ingredient, glue, ties directly to Newell Brands (producer of Elmer’s glue). Social chatter about glue sell-outs suggests unreported Q4 revenue growth, potentially boosting Newell Brands’ stock by the next earnings date. This project automates such trend identification and stock linkage.

## SmolAgents Framework
We use [SmolAgents](https://huggingface.co/docs/smolagents/en/index), a lightweight multi-agent framework from Hugging Face, to orchestrate our workflow. Each agent specializes in a task, passing data sequentially, with iteration driven by a review process.

## Workflow and Agents

![Diagram](rapidreasoning.svg "Multi-Agent Workflow")

1. **Planner Agent**: Interprets the input (e.g., "Find trends impacting stocks since Q3 2023") and delegates tasks via a plan.
2. **Data Collector Agent**: Gathers social data using tools like our custom [TikTok Trending Hashtags Scraper](https://apify.com/lexis-solutions/tiktok-trending-hashtags-scraper) (built with Apify) and web searches.
3. **Developer Agent**: Analyzes trends (e.g., `#slime`) and searches for raw consumer data related to trends.
4. **Consumer Product Agent**: Parses the raw consumer data and creates a list of consumer products.
5. **Supply Chain Agent**: Maps consumer products to supply chains.
6. **Stock Agent**: Uses the supply chains to identify specific companies and stocks to invest in.
7. **Reviewer Agent**: Evaluates the reasoning chain and final result, and decides whether the final list of stocks is sufficient.

The agents pass info in this order, iterating until the Reviewer approves a report with stocks.

## TikTok Tool
We built a custom tool using the [TikTok Trending Hashtags Scraper](https://apify.com/lexis-solutions/tiktok-trending-hashtags-scraper) from Apify to fetch trending hashtags (e.g., `#slime`, 107M views) for the Data Collector Agent, enabling real-time trend analysis. This open-source tool can be used by any smolagents agent.

## Example of what our agents have found
Bhad Babie is trending on tiktok currently.

From news articles our agents found out bhad babie is trending because of a feud with alabama barker.

Our agents found Alabama barker merch as a consumer product.

Alabama barker merch is produced by Zumiez. Zumzie is a publicly traded company, so the final stock the agents recommended was $ZUMZ.

## References
- [SmolAgents Documentation](https://huggingface.co/docs/smolagents/en/index)
- [TikTok Trending Hashtags Scraper](https://apify.com/lexis-solutions/tiktok-trending-hashtags-scraper)
