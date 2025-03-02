# Earnings Day Stock Movement Prediction with Multi-Agent System

This project, developed for a hackathon, leverages a multi-agent system to predict stock price movements on earnings day by identifying unnoticed consumer product trends since the last earnings call. Built using the [Hugging Face SmolAgents framework](https://huggingface.co/docs/smolagents/en/index), it analyzes social data (e.g., TikTok trends) to propose high-conviction stock plays with data-backed theses.

## The Slime Example
Since Q3 2023, the TikTok hashtag `#slime` has surged to 107M views and 16K posts, signaling a slime-making craze. Slime’s key ingredient, glue, ties directly to Newell Brands (producer of Elmer’s glue). Social chatter about glue sell-outs suggests unreported Q4 revenue growth, potentially boosting Newell Brands’ stock by the next earnings date. This project automates such trend identification and stock linkage.

## SmolAgents Framework
We use [SmolAgents](https://huggingface.co/docs/smolagents/en/index), a lightweight multi-agent framework from Hugging Face, to orchestrate our workflow. Each agent specializes in a task, passing data sequentially, with iteration driven by a review process.

## Workflow and Agents

![Diagram](rapidreasoning.svg "Multi-Agent Workflow")

1. **Planner Agent**: Interprets the input (e.g., "Find trends impacting stocks since Q3 2023") and delegates tasks via a plan.
2. **Data Collector Agent**: Gathers social data using tools like our custom [TikTok Trending Hashtags Scraper](https://apify.com/lexis-solutions/tiktok-trending-hashtags-scraper) (built with Apify) and web searches.
3. **Developer Agent**: Analyzes trends (e.g., `#slime`), infers products (e.g., glue), and links to companies (e.g., Newell Brands) with search-backed reasoning.
4. **Interpreter Agent**: Processes and structures data (e.g., parses TikTok JSON, local HTML) for downstream agents.
5. **Supply Chain Agent**: Maps trends to supply chain impacts (e.g., glue production for Newell Brands).
6. **Stock Agent**: Assesses stock movement potential (e.g., Q4 revenue uplift) using company financial context.
7. **Reviewer Agent**: Evaluates the thesis for logic, evidence, and novelty; accepts it or sends it back to the Planner for edits.

The agents pass info in this order, iterating until the Reviewer approves a concise report with 1-2 high-conviction plays.

## TikTok Tool
We built a custom tool using the [TikTok Trending Hashtags Scraper](https://apify.com/lexis-solutions/tiktok-trending-hashtags-scraper) from Apify to fetch trending hashtags (e.g., `#slime`, 107M views) for the Data Collector Agent, enabling real-time trend analysis.

## References
- [SmolAgents Documentation](https://huggingface.co/docs/smolagents/en/index)
- [TikTok Trending Hashtags Scraper](https://apify.com/lexis-solutions/tiktok-trending-hashtags-scraper)
