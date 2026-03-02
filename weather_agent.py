import os
import requests, json
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv(override=True)

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

@tool
def get_weather(location):
    '''
    
    此函數調用 OpenWeatherMap API 來獲取指定位置的當前天氣數據。
    
    參數:
        location (str): 城市名稱或地點名稱，用於查詢天氣資訊
        
    返回:
        str: 包含天氣資訊的 JSON 字符串，包括溫度、濕度、風速、天氣狀況等數據
             如果 API 請求失敗，返回 None
             
    範例:
        >>> result = get_weather("taipei")
        >>> print(result)
        {"coord": {...}, "weather": [...], "main": {"temp": 25.5, ...}}
        
    注意:
        - 需要設置有效的 OPENWEATHERMAP_API_KEY 環境變數
        - 溫度單位為攝氏度 (metric)
        - 返回信息語言設置為繁體中文 (zh_tw)
        - 若地點不存在或 API 請求失敗，函數不會拋出異常
        
    異常:
        - 若 response.status_code 不為 200，函數會默默失敗
    '''

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric",
        "lang": "zh_tw"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)

if __name__ == "__main__":
    from langchain.agents import create_agent
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(model="gpt-5-nano-2025-08-07",)
    agent = create_agent(
        model=model,
        tools=[get_weather],
        system_prompt="你是一名多才多藝的智能助手，可以調用工具幫助用戶解決問題。"
    )
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "請幫我查詢台北的天氣?"}]}
    )
    print(result['messages'][-1].content)