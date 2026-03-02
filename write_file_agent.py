import os
from datetime import datetime
from langchain.tools import tool


@tool
def write_file(content: str) -> str:
    '''
    此函數將接收到的內容寫入一個新的文本文件中，並返回文件的路徑。
    
    參數:
        content (str): 要寫入文件的文本內容
        
    返回:
        str: 包含新創建文件路徑的字符串
        
    範例:
        >>> result = write_file("Hello, world!")
        >>> print(result)
        "Content written to file: /path/to/file_2025-08-07_15-30-00.txt"
        
    注意:
        - 文件將被命名為 "file_YYYY-MM-DD_HH-MM-SS.txt"，其中包含當前日期和時間
        - 文件將被保存在當前工作目錄中
        - 如果寫入過程中發生任何錯誤，函數將返回錯誤信息而不是拋出異常
    '''
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"file_{timestamp}.txt"
        with open(filename, "w") as file:
            file.write(content)
        return f"Content written to file: {os.path.abspath(filename)}"
    except Exception as e:
        return f"Error writing to file: {str(e)}"
    
if __name__ == "__main__":
    from langchain.agents import create_agent
    from langchain_openai import ChatOpenAI
    from dotenv import load_dotenv
    load_dotenv(override=True)
    model = ChatOpenAI(model="gpt-5-nano-2025-08-07",)
    agent = create_agent(
        model=model,
        tools=[write_file],
        system_prompt="你是一名多才多藝的智能助手，可以調用工具幫助用戶解決問題。"
    )
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "請幫我把這段文字寫入一個文件中: Hello, world!"}]}
    )
    print(result['messages'][-1].content)