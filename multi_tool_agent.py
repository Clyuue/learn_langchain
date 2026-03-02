from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from weather_agent import get_weather
from write_file_agent import write_file
load_dotenv(override=True)
model = ChatOpenAI(model="gpt-5-nano-2025-08-07",)
agent = create_agent(
    model=model,
    tools=[get_weather, write_file],
    system_prompt="你是一名多才多藝的智能助手，可以調用工具幫助用戶解決問題。"
)
result = agent.invoke(
    {"messages": [{"role": "user", "content": "請幫我查詢今天台北和高雄天氣哪個溫暖，並將結果記錄在文件中"}]}
)
print(result['messages'][-1].content)