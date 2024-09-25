import datetime

def save_conversation(conversation):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversation_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("结构工具箱项目对话记录\n")
        file.write("=" * 30 + "\n\n")
        for entry in conversation:
            if entry['role'] == 'human':
                file.write("用户: " + entry['content'] + "\n\n")
            elif entry['role'] == 'assistant':
                file.write("助手: " + entry['content'] + "\n\n")
        file.write("=" * 30 + "\n")
        file.write("对话结束")

# 示例对话
conversation = [
    {"role": "human", "content": "网页版的结构工具箱。以下是详细的设计方案:..."},
    {"role": "assistant", "content": "非常感谢您提供的详细设计方案。我理解您想要创建一个网页版的结构工具箱，包含多个功能页面和一个首页。我会根据您的要求提供一些建议和代码示例。..."},
    # ... 添加更多对话内容 ...
]

save_conversation(conversation)
print(f"对话已保存到文件中。")