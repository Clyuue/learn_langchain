import os
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv(override=True)

web_search = TavilySearch(max_results=2)

agent = create_agent(
    "gpt-5-nano-2025-08-07",
    tools = [web_search],
    system_prompt = "你是一名多才多藝的智能助手，可以調用工具幫助用戶解決問題。"
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "請幫我查詢2025年諾貝爾物理學獎得主是誰?"}]}
)
print(result['messages'][-1].content)